"""autoclasswrapper: Python wrapper for AutoClass clustering.

Prepare output files and results
"""

import datetime
import logging
import os
import zipfile

import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hierarchy
import matplotlib.pyplot as plt

log = logging.getLogger(__name__)


class Output():
    """Autoclass output files and results.

    Parameters
    ----------
    root_in_name : string (default: "autoclass")
        Root name to read input files generated by autoclass.
        Example: "autoclass" will lead to "autoclass.db2",
        "autoclass.model", "autoclass.s-params"...
    root_out_name : string (default: "autoclass_out")
        Root name to write output files
        Ex.: "autoclass_out" will lead to "autoclass_out.cdt",
        "autoclass_out_stats.tsv"
    tolerate_error : bool (default: False)
        If True, countinue generation of autoclass input files even if an
        error is encounter.
        If False, stop at first error.

    Attributes
    ----------
    had_error : bool (defaut False)
        Set to True if an error has been found in the generation of autoclass
        input files.
    case_number : int (default 0)
        Number of cases (i.e. of genes/proteins).
    class_number : int (default 0)
        Number of classes (i.e. clusters).
    stats : Pandas dataframe (default None)
        Dataframe that contains, for all cases, main class and probability
        for all classes.
    df : Pandas dataframe (default None)
        Dataframe that contains initial input data and associated clusters.
    experiment_names : list of string (defaut [])
        List of experiment (conditions) names.
        Corresponds to columns in the input data.

    """

    def __init__(self,
                 root_in_name="autoclass",
                 root_out_name="autoclass_out",
                 tolerate_error=False):
        """Instantiate object."""
        self.root_in_name = root_in_name
        self.root_out_name = root_out_name
        self.tolerate_error = tolerate_error
        self.had_error = False
        self.case_number = 0
        self.class_number = 0
        self.stats = None
        self.df = None
        self.experiment_names = []

    def handle_error(f):
        """Handle error during data parsing and formating.

        Function decorator.

        Parameters
        ----------
        f : function

        Returns
        -------
        try_function : function wrapped into error handler

        """
        def try_function(self, *args, **kwargs):
            if self.tolerate_error or not self.had_error:
                try:
                    return f(self, *args, **kwargs)
                except Exception as e:
                    for line in str(e).split('\n'):
                        log.error(line)
                    self.had_error = True
        try_function.__name__ = f.__name__
        try_function.__doc__ = f.__doc__
        return try_function

    @handle_error
    def extract_results(self):
        """Extract results from autoclass.

        Results extracted are:
        - Number of cases (i.e. genes/proteins)
        - Number of classes (i.e. clusters)
        - For each case X, most probable class
        - For each case X, probability to belong to class Y
        """
        log.info("Extracting autoclass results")
        case_name = self.root_in_name + ".case-data-1"
        # first pass:
        # - get number of cases and classes
        # - create empty dataframe to store class/cluster probability
        #   for all cases (i.e gene/protein)
        classes = set()
        with open(case_name, 'r') as case_file:
            for line in case_file:
                if not line:
                    continue
                if line.startswith('#') or line.startswith('DATA'):
                    continue
                items = line.split()
                classes.add(int(items[1]))
                self.case_number += 1
            self.class_number = len(classes)
        log.info("Found {} cases classified in {} classes"
                 .format(self.case_number, self.class_number))
        columns = ["main-class", "main-class-proba"]
        for i in range(self.class_number):
            columns.append("class-{}-proba".format(i+1))
        self.stats = pd.DataFrame(0.0,
                                  index=np.arange(1, self.case_number+1),
                                  columns=columns)
        # second pass: fill the dataframe
        with open(case_name, "r") as case_file:
            for line in case_file:
                if not line:
                    continue
                if line.startswith("#") or line.startswith("DATA"):
                    continue
                items = line.split()
                assert len(items) >= 0, \
                    ("Need case#, class and prob in {}:\n "
                     "{}\n"
                     .format(input_file, line.rstrip()))
                case = int(items[0])
                for idx in range(1, len(items), 2):
                    class_id = int(items[idx]) + 1
                    proba = float(items[idx+1])
                    if idx == 1:
                        self.stats.loc[case, "main-class"] = class_id
                        self.stats.loc[case, "main-class-proba"] = proba
                    label = "class-{}-proba".format(class_id)
                    self.stats.loc[case, label] = proba
        # cast class id to int
        self.stats["main-class"] = self.stats["main-class"].astype(int)

    @handle_error
    def aggregate_input_data(self):
        """Aggregate autoclass classes with input data."""
        log.info("Aggregating input data")
        input_name = self.root_in_name + ".tsv"
        self.df = pd.read_table(input_name, sep="\t", header=0, index_col=0)
        nrows, ncols = self.df.shape
        self.experiment_names = list(self.df.columns)
        assert len(self.stats.index) == nrows, \
            ("Number of cases found in results ({}) "
             "should match number of rows in input file ({})!"
             .format(len(self.stats.index), input_name))
        self.stats.index = self.df.index
        self.df = pd.concat([self.df, self.stats], axis=1)
        # prepare data for export
        log.info("Writing classes + probabilities .tsv file")
        self.df.to_csv(self.root_out_name + ".tsv",
                       sep="\t",
                       header=True,
                       index=True)

    @handle_error
    def write_cdt(self, with_proba=False):
        """Write .cdt file for visualisation.

        Parameters
        ----------
        with_proba : bool (default False)
            If True, also writes probability of case to belong to each class.

        """
        df_tmp = self.df.copy(deep=True)
        if not with_proba:
            log.info("Writing .cdt file")
            filename = self.root_out_name + ".cdt"
        else:
            log.info("Writing .cdt file (with probabilities)")
            filename = self.root_out_name + "_withproba.cdt"
        # add GWEIGHT
        df_tmp["gweight"] = 1
        # add gene name twice for formatting purpose
        df_tmp["name1"] = df_tmp.index
        df_tmp["name2"] = df_tmp.index
        # build gid
        df_tmp["idx"] = np.arange(1, df_tmp.shape[0]+1, dtype=int)
        df_tmp["gid"] = df_tmp.apply(
            lambda x: "GENE{:04d}-CL{:03.0f}X".format(x["idx"],
                                                      x["main-class"]),
            axis=1)
        # sort by increasing class
        df_tmp.sort_values(by=["main-class", "main-class-proba"],
                           ascending=[True, False],
                           inplace=True)
        with open(filename, "w") as cdtfile:
            # write header line
            headers = ["GID", "UNIQID", "NAME", "GWEIGHT"]
            headers += self.experiment_names
            if with_proba:
                headers += ["class-{}-proba"
                            .format(i+1) for i in range(self.class_number)]
            cdtfile.write("{}\n".format("\t".join(headers)))
            # write 'EWEIGHT' line
            eweight = "EWEIGHT\t\t\t"+"\t1"*len(self.experiment_names)
            if with_proba:
                eweight += "\t1"*self.class_number
            cdtfile.write(eweight + "\n")
            # write classes
            col_names = ["gid", "name1", "name2", "gweight"]
            col_names += self.experiment_names
            if with_proba:
                col_names += ["class-{}-proba"
                              .format(i+1) for i in range(self.class_number)]
            for class_idx in range(1, self.class_number+1):
                cluster = df_tmp[df_tmp["main-class"] == class_idx]
                cdtfile.write(cluster.to_csv(sep="\t",
                                             columns=col_names,
                                             index=False,
                                             header=False,
                                             na_rep=""))
                # add spacer between clusters
                for dummy in range(1, 6):
                    cdtfile.write("GENE{:04d}-{:03.0f}S\n"
                                  .format(dummy, class_idx))

    @handle_error
    def write_class_stats(self):
        """Write class stat file.

        Number of elements per class.
        Mean and standard deviation values per experiment.
        """
        log.info("Writing class statistics")
        stat_name = self.root_out_name + "_stats.tsv"
        df_tmp = self.df[["main-class"] + self.experiment_names]
        # compute metrics
        df_count = df_tmp.groupby("main-class").count()
        df_count["stat"] = "count"
        df_mean = df_tmp.groupby("main-class").mean()
        df_mean["stat"] = "mean"
        df_std = df_tmp.groupby("main-class").std()
        df_std["stat"] = "std"
        # concat
        df_stats = pd.concat([df_count, df_mean, df_std], axis=0, join="inner")
        # add cluster
        df_stats["class"] = df_stats.index
        # sort by cluster and metric
        df_stats.sort_values(by=["class", "stat"], inplace=True)
        # save file with ordered columns
        col = list(df_stats.columns)
        df_stats = df_stats[[col[-1], col[-2], *col[:-2]]]
        df_stats.to_csv(stat_name, sep="\t", header=True, index=False)

    @handle_error
    def write_dendrogram(self):
        """Write dendrogram of hierarchical clustering of classes to file."""
        log.info("Writing dendrogram")
        stat_name = self.root_out_name + "_stats.tsv"
        if not os.path.exists(stat_name):
            log.error("Cannot find {}".format(stat_name))
            return 0
        df = pd.read_csv(stat_name, sep="\t")
        # keep only 'mean'
        df = df[df["stat"] == "mean"]
        # remove NA
        df.dropna(inplace=True)
        # keep cluster labels
        labels = df["class"]
        # remove unwanted columns
        df.drop(labels=["stat", "class"], axis=1, inplace=True)
        Z = hierarchy.linkage(df, 'ward')
        plt.figure(figsize=(10, 6))
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Class #')
        plt.ylabel('Distance')
        hierarchy.dendrogram(
            Z,
            color_threshold=0.0,
            above_threshold_color='grey',
            labels=["{:.0f}".format(clust) for clust in labels])
        plt.savefig(self.root_out_name + "_dendrogram.png")

    @handle_error
    def wrap_outputs(self):
        """Wrap results into a zipped file.

        Returns
        -------
        zipname : string
            Name of the zip file that contains output files

        """
        t = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        zipname = "{}-autoclass-clust.zip".format(t)
        with zipfile.ZipFile(zipname, "w") as outputzip:
            for extension in (".tsv", ".cdt", "_withproba.cdt",
                              "_stats.tsv", "_dendrogram.png"):
                filename = self.root_out_name + extension
                if os.path.exists(filename):
                    outputzip.write(filename)
                    log.info("{} added to zip file".format(filename))
        return zipname
