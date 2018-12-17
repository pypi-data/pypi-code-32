# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class MergeModelsInputSpec(CommandLineInputSpec):
    Model1 = File(position=-3, desc="Model", exists=True, argstr="%s")
    Model2 = File(position=-2, desc="Model", exists=True, argstr="%s")
    ModelOutput = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Model",
        argstr="%s")


class MergeModelsOutputSpec(TraitedSpec):
    ModelOutput = File(position=-1, desc="Model", exists=True)


class MergeModels(SEMLikeCommandLine):
    """title: Merge Models

category: Surface Models

description: Merge the polydata from two input models and output a new model with the added polydata. Uses the vtkAppendPolyData filter. Works on .vtp and .vtk surface files.

version: $Revision$

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/MergeModels

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH), Daniel Haehn (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = MergeModelsInputSpec
    output_spec = MergeModelsOutputSpec
    _cmd = "MergeModels "
    _outputs_filenames = {'ModelOutput': 'ModelOutput.vtk'}


class ModelToLabelMapInputSpec(CommandLineInputSpec):
    distance = traits.Float(desc="Sample distance", argstr="--distance %f")
    InputVolume = File(
        position=-3, desc="Input volume", exists=True, argstr="%s")
    surface = File(position=-2, desc="Model", exists=True, argstr="%s")
    OutputVolume = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="The label volume",
        argstr="%s")


class ModelToLabelMapOutputSpec(TraitedSpec):
    OutputVolume = File(position=-1, desc="The label volume", exists=True)


class ModelToLabelMap(SEMLikeCommandLine):
    """title: Model To Label Map

category: Surface Models

description: Intersects an input model with an reference volume and produces an output label map.

version: 0.1.0.$Revision: 8643 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/PolyDataToLabelMap

contributor: Nicole Aucoin (SPL, BWH), Xiaodong Tao (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = ModelToLabelMapInputSpec
    output_spec = ModelToLabelMapOutputSpec
    _cmd = "ModelToLabelMap "
    _outputs_filenames = {'OutputVolume': 'OutputVolume.nii'}


class GrayscaleModelMakerInputSpec(CommandLineInputSpec):
    InputVolume = File(
        position=-2,
        desc="Volume containing the input grayscale data.",
        exists=True,
        argstr="%s")
    OutputGeometry = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Output that contains geometry model.",
        argstr="%s")
    threshold = traits.Float(
        desc=
        "Grayscale threshold of isosurface. The resulting surface of triangles separates the volume into voxels that lie above (inside) and below (outside) the threshold.",
        argstr="--threshold %f")
    name = traits.Str(desc="Name to use for this model.", argstr="--name %s")
    smooth = traits.Int(
        desc="Number of smoothing iterations. If 0, no smoothing will be done.",
        argstr="--smooth %d")
    decimate = traits.Float(
        desc=
        "Target reduction during decimation, as a decimal percentage reduction in the number of polygons. If 0, no decimation will be done.",
        argstr="--decimate %f")
    splitnormals = traits.Bool(
        desc=
        "Splitting normals is useful for visualizing sharp features. However it creates holes in surfaces which affect measurements",
        argstr="--splitnormals ")
    pointnormals = traits.Bool(
        desc=
        "Calculate the point normals? Calculated point normals make the surface appear smooth. Without point normals, the surface will appear faceted.",
        argstr="--pointnormals ")


class GrayscaleModelMakerOutputSpec(TraitedSpec):
    OutputGeometry = File(
        position=-1, desc="Output that contains geometry model.", exists=True)


class GrayscaleModelMaker(SEMLikeCommandLine):
    """title: Grayscale Model Maker

category: Surface Models

description: Create 3D surface models from grayscale data. This module uses Marching Cubes to create an isosurface at a given threshold. The resulting surface consists of triangles that separate a volume into regions below and above the threshold. The resulting surface can be smoothed and decimated. This model works on continuous data while the module Model Maker works on labeled (or discrete) data.

version: 3.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/GrayscaleModelMaker

license: slicer3

contributor: Nicole Aucoin (SPL, BWH), Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = GrayscaleModelMakerInputSpec
    output_spec = GrayscaleModelMakerOutputSpec
    _cmd = "GrayscaleModelMaker "
    _outputs_filenames = {'OutputGeometry': 'OutputGeometry.vtk'}


class ProbeVolumeWithModelInputSpec(CommandLineInputSpec):
    InputVolume = File(
        position=-3,
        desc="Volume to use to 'paint' the model",
        exists=True,
        argstr="%s")
    InputModel = File(
        position=-2, desc="Input model", exists=True, argstr="%s")
    OutputModel = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Output 'painted' model",
        argstr="%s")


class ProbeVolumeWithModelOutputSpec(TraitedSpec):
    OutputModel = File(position=-1, desc="Output 'painted' model", exists=True)


class ProbeVolumeWithModel(SEMLikeCommandLine):
    """title: Probe Volume With Model

category: Surface Models

description: Paint a model by a volume (using vtkProbeFilter).

version: 0.1.0.$Revision: 1892 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/ProbeVolumeWithModel

contributor: Lauren O'Donnell (SPL, BWH)

acknowledgements: BWH, NCIGT/LMI

"""

    input_spec = ProbeVolumeWithModelInputSpec
    output_spec = ProbeVolumeWithModelOutputSpec
    _cmd = "ProbeVolumeWithModel "
    _outputs_filenames = {'OutputModel': 'OutputModel.vtk'}


class LabelMapSmoothingInputSpec(CommandLineInputSpec):
    labelToSmooth = traits.Int(
        desc=
        "The label to smooth.  All others will be ignored.  If no label is selected by the user, the maximum label in the image is chosen by default.",
        argstr="--labelToSmooth %d")
    numberOfIterations = traits.Int(
        desc="The number of iterations of the level set AntiAliasing algorithm",
        argstr="--numberOfIterations %d")
    maxRMSError = traits.Float(
        desc="The maximum RMS error.", argstr="--maxRMSError %f")
    gaussianSigma = traits.Float(
        desc="The standard deviation of the Gaussian kernel",
        argstr="--gaussianSigma %f")
    inputVolume = File(
        position=-2,
        desc="Input label map to smooth",
        exists=True,
        argstr="%s")
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Smoothed label map",
        argstr="%s")


class LabelMapSmoothingOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Smoothed label map", exists=True)


class LabelMapSmoothing(SEMLikeCommandLine):
    """title: Label Map Smoothing

category: Surface Models

description: This filter smoothes a binary label map.  With a label map as input, this filter runs an anti-alising algorithm followed by a Gaussian smoothing algorithm.  The output is a smoothed label map.

version: 1.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/LabelMapSmoothing

contributor: Dirk Padfield (GE), Josh Cates (Utah), Ross Whitaker (Utah)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  This filter is based on work developed at the University of Utah, and implemented at GE Research.

"""

    input_spec = LabelMapSmoothingInputSpec
    output_spec = LabelMapSmoothingOutputSpec
    _cmd = "LabelMapSmoothing "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class ModelMakerInputSpec(CommandLineInputSpec):
    InputVolume = File(
        position=-1,
        desc=
        "Input label map. The Input Volume drop down menu is populated with the label map volumes that are present in the scene, select one from which to generate models.",
        exists=True,
        argstr="%s")
    color = File(
        desc="Color table to make labels to colors and objects",
        exists=True,
        argstr="--color %s")
    modelSceneFile = traits.Either(
        traits.Bool,
        InputMultiPath(File(), ),
        hash_files=False,
        desc=
        "Generated models, under a model hierarchy node. Models are imported into Slicer under a model hierarchy node, and their colors are set by the color table associated with the input label map volume. The model hierarchy node must be created before running the model maker, by selecting Create New ModelHierarchy from the Models drop down menu. If you're running from the command line, a model hierarchy node in a new mrml scene will be created for you.",
        argstr="--modelSceneFile %s...")
    name = traits.Str(
        desc=
        "Name to use for this model. Any text entered in the entry box will be the starting string for the created model file names. The label number and the color name will also be part of the file name. If making multiple models, use this as a prefix to the label and color name.",
        argstr="--name %s")
    generateAll = traits.Bool(
        desc=
        "Generate models for all labels in the input volume. select this option if you want to create all models that correspond to all values in a labelmap volume (using the Joint Smoothing option below is useful with this option). Ignores Labels, Start Label, End Label settings. Skips label 0.",
        argstr="--generateAll ")
    labels = InputMultiPath(
        traits.Int,
        desc=
        "A comma separated list of label values from which to make models. f you specify a list of Labels, it will override any start/end label settings. If you click Generate All Models it will override the list of labels and any start/end label settings.",
        sep=",",
        argstr="--labels %s")
    start = traits.Int(
        desc=
        "If you want to specify a continuous range of labels from which to generate models, enter the lower label here. Voxel value from which to start making models. Used instead of the label list to specify a range (make sure the label list is empty or it will over ride this).",
        argstr="--start %d")
    end = traits.Int(
        desc=
        "If you want to specify a continuous range of labels from which to generate models, enter the higher label here. Voxel value up to which to continue making models. Skip any values with zero voxels.",
        argstr="--end %d")
    skipUnNamed = traits.Bool(
        desc=
        "Select this to not generate models from labels that do not have names defined in the color look up table associated with the input label map. If true, only models which have an entry in the color table will be generated.  If false, generate all models that exist within the label range.",
        argstr="--skipUnNamed ")
    jointsmooth = traits.Bool(
        desc=
        "This will ensure that all resulting models fit together smoothly, like jigsaw puzzle pieces. Otherwise the models will be smoothed independently and may overlap.",
        argstr="--jointsmooth ")
    smooth = traits.Int(
        desc=
        "Here you can set the number of smoothing iterations for Laplacian smoothing, or the degree of the polynomial approximating the windowed Sinc function. Use 0 if you wish no smoothing. ",
        argstr="--smooth %d")
    filtertype = traits.Enum(
        "Sinc",
        "Laplacian",
        desc=
        "You can control the type of smoothing done on the models by selecting a filter type of either Sinc or Laplacian.",
        argstr="--filtertype %s")
    decimate = traits.Float(
        desc=
        "Chose the target reduction in number of polygons as a decimal percentage (between 0 and 1) of the number of polygons. Specifies the percentage of triangles to be removed. For example, 0.1 means 10% reduction and 0.9 means 90% reduction.",
        argstr="--decimate %f")
    splitnormals = traits.Bool(
        desc=
        "Splitting normals is useful for visualizing sharp features. However it creates holes in surfaces which affects measurements.",
        argstr="--splitnormals ")
    pointnormals = traits.Bool(
        desc=
        "Turn this flag on if you wish to calculate the normal vectors for the points.",
        argstr="--pointnormals ")
    pad = traits.Bool(
        desc=
        "Pad the input volume with zero value voxels on all 6 faces in order to ensure the production of closed surfaces. Sets the origin translation and extent translation so that the models still line up with the unpadded input volume.",
        argstr="--pad ")
    saveIntermediateModels = traits.Bool(
        desc=
        "You can save a copy of the models after each of the intermediate steps (marching cubes, smoothing, and decimation if not joint smoothing, otherwise just after decimation). These intermediate models are not saved in the mrml file, you have to load them manually after turning off deleting temporary files in they python console (View ->Python Interactor) using the following command slicer.modules.modelmaker.cliModuleLogic().DeleteTemporaryFilesOff().",
        argstr="--saveIntermediateModels ")
    debug = traits.Bool(
        desc=
        "turn this flag on in order to see debugging output (look in the Error Log window that is accessed via the View menu)",
        argstr="--debug ")


class ModelMakerOutputSpec(TraitedSpec):
    modelSceneFile = OutputMultiPath(
        File(exists=True),
        desc=
        "Generated models, under a model hierarchy node. Models are imported into Slicer under a model hierarchy node, and their colors are set by the color table associated with the input label map volume. The model hierarchy node must be created before running the model maker, by selecting Create New ModelHierarchy from the Models drop down menu. If you're running from the command line, a model hierarchy node in a new mrml scene will be created for you."
    )


class ModelMaker(SEMLikeCommandLine):
    """title: Model Maker

category: Surface Models

description: Create 3D surface models from segmented data.<p>Models are imported into Slicer under a model hierarchy node in a MRML scene. The model colors are set by the color table associated with the input volume (these colours will only be visible if you load the model scene file).</p><p><b>Create Multiple:</b></p><p>If you specify a list of Labels, it will over ride any start/end label settings.</p><p>If you click<i>Generate All</i>it will over ride the list of lables and any start/end label settings.</p><p><b>Model Maker Settings:</b></p><p>You can set the number of smoothing iterations, target reduction in number of polygons (decimal percentage). Use 0 and 1 if you wish no smoothing nor decimation.<br>You can set the flags to split normals or generate point normals in this pane as well.<br>You can save a copy of the models after intermediate steps (marching cubes, smoothing, and decimation if not joint smoothing, otherwise just after decimation); these models are not saved in the mrml file, turn off deleting temporary files first in the python window:<br><i>slicer.modules.modelmaker.cliModuleLogic().DeleteTemporaryFilesOff()</i></p>

version: 4.1

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/ModelMaker

license: slicer4

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH), Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = ModelMakerInputSpec
    output_spec = ModelMakerOutputSpec
    _cmd = "ModelMaker "
    _outputs_filenames = {'modelSceneFile': 'modelSceneFile.mrml'}
