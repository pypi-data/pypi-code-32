"""
DeepLabCut2.0 Toolbox
https://github.com/AlexEMG/DeepLabCut

A Mathis, alexander.mathis@bethgelab.org
T Nath, nath@rowland.harvard.edu
M Mathis, mackenzie@post.harvard.edu

"""
import numpy as np
import os
from pathlib import Path
import pandas as pd
import statsmodels.api as sm
from deeplabcut.utils import auxiliaryfunctions, visualization
from deeplabcut.utils import frameselectiontools
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
from skimage.util import img_as_ubyte

def extract_outlier_frames(config,videos,shuffle=1,trainingsetindex=0,outlieralgorithm='fitting',comparisonbodyparts='all',epsilon=20,p_bound=.01,ARdegree=3,MAdegree=1,alpha=.01,extractionalgorithm='uniform',automatic=False):
    """
    Extracts the outlier frames in case, the predictions are not correct for a certain video from the cropped video running from
    start to stop as defined in config.yaml.

    Another crucial parameter in config.yaml is how many frames to extract 'numframes2extract'.

    Parameter
    ----------
    config : string
        Full path of the config.yaml file as a string.

    videos: list
        Full path of the video to extract the frame from. Make sure that this video is already analyzed. 

    shuffle : int, optional
        The shufle index of training dataset. The extracted frames will be stored in the labeled-dataset for
        the corresponding shuffle of training dataset. Default is set to 1

    trainingsetindex: int, optional
        Integer specifying which TrainingsetFraction to use. By default the first (note that TrainingFraction is a list in config.yaml).
     
    outlieralgorithm: 'fitting', 'jump', or 'uncertain', optional
        String specifying the algorithm used to detect the outliers. Currently, deeplabcut supports three methods. 'Fitting'
        fits a Auto Regressive Integrated Moving Average model to the data and computes the distance to the estimated data. Larger distances than
        epsilon are then potentially identified as outliers. The methods 'jump' identifies larger jumps than 'epsilon' in any body part; and 'uncertain'
        looks for frames with confidence below p_bound. The default is set to ``fitting``.

    comparisonbodyparts: list of strings, optional
        This select the body parts for which the comparisons with the outliers are carried out. Either ``all``, then all body parts
        from config.yaml are used orr a list of strings that are a subset of the full list.
        E.g. ['hand','Joystick'] for the demo Reaching-Mackenzie-2018-08-30/config.yaml to select only these two body parts.

    p_bound: float between 0 and 1, optional
        For outlieralgorithm 'uncertain' this parameter defines the likelihood below, below which a body part will be flagged as a putative outlier.

    epsilon; float,optional
        Meaning depends on outlieralgoritm. The default is set to 20 pixels.
        For outlieralgorithm 'fitting': Float bound according to which frames are picked when the (average) body part estimate deviates from model fit
        For outlieralgorithm 'jump': Float bound specifying the distance by which body points jump from one frame to next (Euclidean distance)

    ARdegree: int, optional
        For outlieralgorithm 'fitting': Autoregressive degree of ARIMA model degree. (Note we use SARIMAX without exogeneous and seasonal part)
        see https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html

    MAdegree: int
        For outlieralgorithm 'fitting': MovingAvarage degree of ARIMA model degree. (Note we use SARIMAX without exogeneous and seasonal part)
        See https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html

    alpha: float
        Significance level for detecting outliers based on confidence interval of fitted ARIMA model. Only the distance is used however.

    extractionalgorithm : string, optional
        String specifying the algorithm to use for selecting the frames from the identified putatative outlier frames. Currently, deeplabcut
        supports either ``kmeans`` or ``uniform`` based selection (same logic as for extract_frames).
        The default is set to``uniform``, if provided it must be either ``uniform`` or ``kmeans``.
    
    automatic : bool, optional
        Set it to True, if you want to extract outliers without being asked for user feedback. 

    Example
    --------
    for extracting the frames with default settings
    >>> deeplabcut.extract_outlier_frames('/analysis/project/reaching-task/config.yaml',['/analysis/project/video/reachinvideo1.avi'])
    --------
    for extracting the frames with kmeans
    >>> deeplabcut.extract_outlier_frames('/analysis/project/reaching-task/config.yaml',['/analysis/project/video/reachinvideo1.avi'],extractionalgorithm='kmeans')
    --------
    for extracting the frames with kmeans and epsilon = 5 pixels.
    >>> deeplabcut.extract_outlier_frames('/analysis/project/reaching-task/config.yaml',['/analysis/project/video/reachinvideo1.avi'],epsilon = 5,extractionalgorithm='kmeans')
    --------
    """

    cfg = auxiliaryfunctions.read_config(config)
    scorer=auxiliaryfunctions.GetScorerName(cfg,shuffle,trainFraction = cfg['TrainingFraction'][trainingsetindex])
    print("network parameters:", scorer)
    for video in videos:
      videofolder = str(Path(video).parents[0])
      dataname = str(Path(video).stem)+scorer
      try:
          Dataframe = pd.read_hdf(os.path.join(videofolder,dataname+'.h5'))
          nframes=np.size(Dataframe.index)
          #extract min and max index based on start stop interval.
          startindex=max([int(np.floor(nframes*cfg['start'])),0])
          stopindex=min([int(np.ceil(nframes*cfg['stop'])),nframes])
          Index=np.arange(stopindex-startindex)+startindex
  
          #figure out body part list:
          bodyparts=auxiliaryfunctions.IntersectionofBodyPartsandOnesGivenbyUser(cfg,comparisonbodyparts)
  
          Indices=[]
          if outlieralgorithm=='uncertain': #necessary parameters: considered body parts and
              for bpindex,bp in enumerate(bodyparts):
                  if bp in cfg['bodyparts']: #filter [who knows what users put in...]
                      p=Dataframe[scorer][bp]['likelihood'].values[Index]
                      Indices.extend(np.where(p<p_bound)[0]+startindex) # all indices between start and stop that are below p_bound.
  
          elif outlieralgorithm=='jump':
              for bpindex,bp in enumerate(bodyparts):
                  if bp in cfg['bodyparts']: #filter [who knows what users put in...]
                      dx=np.diff(Dataframe[scorer][bp]['x'].values[Index])
                      dy=np.diff(Dataframe[scorer][bp]['y'].values[Index])
                      # all indices between start and stop with jump larger than epsilon (leading up to this point!)
                      Indices.extend(np.where((dx**2+dy**2)>epsilon**2)[0]+startindex+1) 
  
          elif outlieralgorithm=='fitting':
              #deviation_dataname = str(Path(videofolder)/Path(dataname))
              # Calculate deviatons for video
              [d,o] = ComputeDeviations(Dataframe,cfg,comparisonbodyparts,scorer,dataname,p_bound,alpha,ARdegree,MAdegree)
              #Some heuristics for extracting frames based on distance:
              Indices=np.where(d>epsilon)[0] # time points with at least average difference of epsilon
              
              if len(Index)<cfg['numframes2pick']*2 and len(d)>cfg['numframes2pick']*2: # if too few points qualify, extract the most distant ones.
                  Indices=np.argsort(d)[::-1][:cfg['numframes2pick']*2]
  
          Indices=np.sort(list(set(Indices))) #remove repetitions.
          print("Method ", outlieralgorithm, " found ", len(Indices)," putative outlier frames.")
          print("Do you want to proceed with extracting ", cfg['numframes2pick'], " of those?")
          if outlieralgorithm=='uncertain':
              print("If this list is very large, perhaps consider changing the paramters (start, stop, p_bound, comparisonbodyparts) or use a different method.")
          elif outlieralgorithm=='jump':
              print("If this list is very large, perhaps consider changing the paramters (start, stop, epsilon, comparisonbodyparts) or use a different method.")
          elif outlieralgorithm=='fitting':
              print("If this list is very large, perhaps consider changing the paramters (start, stop, epsilon, ARdegree, MAdegree, alpha, comparisonbodyparts) or use a different method.")
  
          if automatic==False:
              askuser = input("yes/no")
          else:
              askuser='Ja'
              
          if askuser=='y' or askuser=='yes' or askuser=='Ja' or askuser=='ha': # multilanguage support :)
              #Now extract from those Indices!
              ExtractFramesbasedonPreselection(Indices,extractionalgorithm,Dataframe,dataname,scorer,video,cfg,config)
          else:
              print("Nothing extracted, change parameters and start again...")
  
      except FileNotFoundError:
          print("The video has not been analyzed yet!. You can only refine the labels, after the pose has been estimate. Please run 'analyze_video' first.")


def filterpredictions(config,video,shuffle=1,trainingsetindex=0,comparisonbodyparts='all',p_bound=.01,ARdegree=3,MAdegree=1,alpha=.01):
    """
    Fits frame-by-frame pose predictions with SARIMAX model.

    Parameter
    ----------
    config : string
        Full path of the config.yaml file as a string.

    video : string
        Full path of the video to extract the frame from. Make sure that this video is already analyzed.

    shuffle : int, optional
        The shufle index of training dataset. The extracted frames will be stored in the labeled-dataset for
        the corresponding shuffle of training dataset. Default is set to 1

    trainingsetindex: int, optional
        Integer specifying which TrainingsetFraction to use. By default the first (note that TrainingFraction is a list in config.yaml).
     
    comparisonbodyparts: list of strings, optional
        This select the body parts for which SARIMAX models are fit. Either ``all``, then all body parts
        from config.yaml are used orr a list of strings that are a subset of the full list.
        E.g. ['hand','Joystick'] for the demo Reaching-Mackenzie-2018-08-30/config.yaml to select only these two body parts.

    p_bound: float between 0 and 1, optional
        For outlieralgorithm 'uncertain' this parameter defines the likelihood below, below which a body part will be flagged as a putative outlier.

    ARdegree: int, optional
        For outlieralgorithm 'fitting': Autoregressive degree of Sarimax model degree.
        see https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html

    MAdegree: int
        For outlieralgorithm 'fitting': Moving Avarage degree of Sarimax model degree.
        See https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html

    alpha: float
        Significance level for detecting outliers based on confidence interval of fitted SARIMAX model.
    
    Example
    --------
    tba
    --------
    
    Returns filtered pandas array (incl. confidence interval), original data, distance and average outlier vector.
    
    """

    cfg = auxiliaryfunctions.read_config(config)
    scorer=auxiliaryfunctions.GetScorerName(cfg,shuffle,trainFraction = cfg['TrainingFraction'][trainingsetindex])
    print("network parameters:", scorer)
    videofolder = str(Path(video).parents[0])
    dataname = str(Path(video).stem)+scorer
    bodyparts=auxiliaryfunctions.IntersectionofBodyPartsandOnesGivenbyUser(cfg,comparisonbodyparts)
    try:
        Dataframe = pd.read_hdf(os.path.join(videofolder,dataname+'.h5'))
    except FileExistsError:
        print("Could not find data.")
    
    data,d,o = ComputeDeviations(Dataframe,cfg,bodyparts,scorer,dataname,p_bound,alpha,ARdegree,MAdegree,storeoutput='full')
    return data,Dataframe,d,o

def convertparms2start(pn):
    ''' Creating a start value for sarimax in case of an value error 
    See: https://groups.google.com/forum/#!topic/pystatsmodels/S_Fo53F25Rk '''
    if 'ar.' in pn:
        return 0
    elif 'ma.' in pn:
        return 0
    elif 'sigma' in pn:
        return 1
    else:
        return 0

def FitSARIMAXModel(x,p,pcutoff,alpha,ARdegree,MAdegree,nforecast = 0):
    # Seasonal Autoregressive Integrated Moving-Average with eXogenous regressors (SARIMAX)
    # see http://www.statsmodels.org/stable/statespace.html#seasonal-autoregressive-integrated-moving-average-with-exogenous-regressors-sarimax
    Y=x.copy()
    Y[p<pcutoff]=np.nan # Set uncertain estimates to nan (modeled as missing data)
    if np.sum(np.isfinite(Y))>10:
        
        # SARIMAX implemetnation has better prediction models than simple ARIMAX (however we do not use the seasonal etc. parameters!)
        mod = sm.tsa.statespace.SARIMAX(Y.flatten(), order=(ARdegree,0,MAdegree),seasonal_order=(0, 0, 0, 0),simple_differencing=True)
        #Autoregressive Moving Average ARMA(p,q) Model
        #mod = sm.tsa.ARIMA(Y, order=(ARdegree,0,MAdegree)) #order=(ARdegree,0,MAdegree)
        try:
            res = mod.fit(disp=True)
        except ValueError: #https://groups.google.com/forum/#!topic/pystatsmodels/S_Fo53F25Rk (let's update to statsmodels 0.10.0 soon...)
            startvalues=np.array([convertparms2start(pn) for pn in mod.param_names])
            res= mod.fit(start_params=startvalues,disp=True)
            
        predict = res.get_prediction(end=mod.nobs + nforecast-1)
        return predict.predicted_mean,predict.conf_int(alpha=alpha)
    else:
        return np.nan*np.zeros(len(Y)),np.nan*np.zeros((len(Y),2))
    
def ComputeDeviations(Dataframe,cfg,comparisonbodyparts,scorer,dataname,p_bound,alpha,ARdegree,MAdegree,storeoutput=None):
    ''' Fits Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors model to data and computes confidence interval
    as well as mean fit. '''

    print("Fitting state-space models with parameters", ARdegree,MAdegree)
    bpindex=0
    ntimes=np.size(Dataframe.index)
    
    for bp in tqdm(comparisonbodyparts):
        if bp in cfg['bodyparts']: #filter [who knows what users put in...]
            x,y,p=Dataframe[scorer][bp]['x'].values,Dataframe[scorer][bp]['y'].values,Dataframe[scorer][bp]['likelihood'].values
            meanx,CIx=FitSARIMAXModel(x,p,p_bound,alpha,ARdegree,MAdegree)
            #meanx,CIx=meanx.values,CIx.values
            meany,CIy=FitSARIMAXModel(y,p,p_bound,alpha,ARdegree,MAdegree)
            #meany,CIy=meany.values,CIy.values
            '''
            try:
                meanx,CIx=FitSARIMAXModel(x,p,p_bound,alpha,ARdegree,MAdegree)
                meanx,CIx=meanx,CIx
            except ValueError:
                meanx,CIx=np.nan*np.zeros(ntimes),np.nan*np.zeros((ntimes,2)) 
            try:
                meany,CIy=FitSARIMAXModel(y,p,p_bound,alpha,ARdegree,MAdegree)
                meany,CIy=meany,CIy
            except ValueError:
                meany,CIy=np.nan*np.zeros(ntimes),np.nan*np.zeros((ntimes,2))
            '''
            if storeoutput=='full': #stores both the means and the confidence interval (as well as the summary stats below)
            
                pdindex = pd.MultiIndex.from_product(
                    [[scorer], [bp], ['meanx', 'meany','lowerCIx','higherCIx', 'lowerCIy','higherCIy']],
                    names=['scorer', 'bodyparts', 'coords'])

                if bpindex==0:
                    data = pd.DataFrame(np.hstack([np.expand_dims(meanx,axis=1),np.expand_dims(meany,axis=1),CIx,CIy]), columns=pdindex)
                else:
                    item=pd.DataFrame(np.hstack([np.expand_dims(meanx,axis=1),np.expand_dims(meany,axis=1),CIx,CIy]), columns=pdindex)
                    data=pd.concat([data.T, item.T]).T

            pdindex = pd.MultiIndex.from_product([[scorer], [bp], ['distance','significant']],names=['scorer', 'bodyparts', 'coords'])
            distance=np.sqrt((x-meanx)**2+(y-meany)**2)
            significant=(x<CIx[:,0])+(x>CIx[:,1])+(x<CIy[:,0])+(y>CIy[:,1])

            if bpindex==0:
                data = pd.DataFrame(np.hstack([distance[:,np.newaxis],significant[:,np.newaxis]]), columns=pdindex)
            else:
                item=pd.DataFrame(np.hstack([distance[:,np.newaxis],significant[:,np.newaxis]]), columns=pdindex)
                data=pd.concat([data.T, item.T]).T
            bpindex+=1
            
    bpindex=0
    for bp in comparisonbodyparts: #calculate # outliers & and average distance.
        if bp in cfg['bodyparts']: #filter [who knows what users put in...]
            if bpindex==0:
                d=data[scorer][bp]["distance"]
                o=data[scorer][bp]["significant"]
            else:
                d+=data[scorer][bp]["distance"]
                o+=data[scorer][bp]["significant"]
            bpindex+=1
    
    if storeoutput=='full':
        data.to_hdf(dataname.split('.h5')[0]+'filtered.h5', 'df_with_missing', format='table', mode='w')
        #data.to_csv(dataname.split('.h5')[0]+'filtered.csv')
        
        if bpindex!=0:
            return data,d*1./bpindex,o*1./bpindex #average distance and average # significant differences avg. over comparisonbodyparts
        else:
            return data,np.zeros(ntimes), np.zeros(ntimes) 
    else:
        if bpindex!=0:
            return d*1./bpindex,o*1./bpindex #average distance and average # significant differences avg. over comparisonbodyparts
        else:
            return np.zeros(ntimes), np.zeros(ntimes) 


def ExtractFramesbasedonPreselection(Index,extractionalgorithm,Dataframe,dataname,scorer,video,cfg,config):
    from deeplabcut.create_project import add
    start  = cfg['start']
    stop = cfg['stop']
    numframes2extract = cfg['numframes2pick']
    bodyparts=cfg['bodyparts']

    videofolder = str(Path(video).parents[0])
    vname = str(Path(video).stem)
    tmpfolder = os.path.join(cfg['project_path'],'labeled-data', vname)
    if os.path.isdir(tmpfolder):
        print("Frames from video", vname, " already extracted (more will be added)!")
    else:
        auxiliaryfunctions.attempttomakefolder(tmpfolder)

    print("Loading video...")
    clip = VideoFileClip(video)
    fps = clip.fps
    nframes = np.size(Dataframe.index)

    if  cfg['cropping']:  # one might want to adjust
        clip = clip.crop(y1=cfg['y1'], y2=cfg['x2'], x1=cfg['x1'], x2=cfg['x2'])
        coords = (cfg['x1'],cfg['x2'],cfg['y1'], cfg['y2'])
    else:
        coords = None
    print("Duration of video [s]: ", clip.duration, ", recorded @ ", fps,"fps!")
    print("Overall # of frames: ", nframes, "with (cropped) frame dimensions: ",clip.size)
    if extractionalgorithm=='uniform':
        frames2pick=frameselectiontools.UniformFrames(clip,numframes2extract,start,stop,Index)
    elif extractionalgorithm=='kmeans':
        frames2pick=frameselectiontools.KmeansbasedFrameselection(clip,numframes2extract,start,stop,Index)
    else:
        print("Please implement this method yourself!")
        frames2pick=[]

    # Extract frames + frames with plotted labels and store them in folder (with name derived from video name) nder labeled-data
    print("Let's select frames indices:", frames2pick)
    colors = visualization.get_cmap(len(bodyparts),cfg['colormap'])
    strwidth = int(np.ceil(np.log10(nframes))) #width for strings
    for index in frames2pick: ##tqdm(range(0,nframes,10)):
        PlottingSingleFrame(clip,Dataframe,bodyparts,tmpfolder,index,scorer,cfg['dotsize'],cfg['pcutoff'],cfg['alphavalue'],colors,strwidth)
        plt.close("all")

    #close videos
    clip.close()
    del clip

    # Extract annotations based on DeepLabCut and store in the folder (with name derived from video name) under labeled-data
    if len(frames2pick)>0:
        Dataframe = pd.read_hdf(os.path.join(videofolder,dataname+'.h5'))
        DF = Dataframe.ix[frames2pick]
        DF.index=[os.path.join('labeled-data', vname,"img"+str(index).zfill(strwidth)+".png") for index in DF.index] #exchange index number by file names.
    
        machinefile=os.path.join(tmpfolder,'machinelabels-iter'+str(cfg['iteration'])+'.h5')
        if Path(machinefile).is_file():
            Data = pd.read_hdf(machinefile, 'df_with_missing')
            DataCombined = pd.concat([Data, DF])
            #drop duplicate labels:
            DataCombined = DataCombined[~DataCombined.index.duplicated(keep='first')]
            
            DataCombined.to_hdf(machinefile, key='df_with_missing', mode='w')
            DataCombined.to_csv(os.path.join(tmpfolder, "machinelabels.csv")) #this is always the most current one (as reading is from h5)
        else:
            DF.to_hdf(machinefile,key='df_with_missing',mode='w')
            DF.to_csv(os.path.join(tmpfolder, "machinelabels.csv"))
        try:
          add.add_new_videos(config,[video],coords=[coords]) # make sure you pass coords as a list 
        except: #can we make a catch here? - in fact we should drop indices from DataCombined if they are in CollectedData.. [ideal behavior; currently this is pretty unlikely]
            print("AUTOMATIC ADDING OF VIDEO TO CONFIG FILE FAILED! You need to do this manually for including it in the config.yaml file!")
            print("Videopath:", video,"Coordinates for cropping:", coords)
            pass
      
        print("The outlier frames are extracted. They are stored in the subdirectory labeled-data\%s."%vname)
        print("Once you extracted frames for all videos, use 'refine_labels' to manually correct the labels.")
    else:
        print("No frames were extracted.")
        
def PlottingSingleFrame(clip,Dataframe,bodyparts2plot,tmpfolder,index,scorer,dotsize,pcutoff,alphavalue,colors,strwidth=4):
        ''' Label frame and save under imagename '''
        from skimage import io
        imagename1 = os.path.join(tmpfolder,"img"+str(index).zfill(strwidth)+".png")
        imagename2 = os.path.join(tmpfolder,"img"+str(index).zfill(strwidth)+"labeled.png")

        if os.path.isfile(os.path.join(tmpfolder,"img"+str(index).zfill(strwidth)+".png")):
            pass
        else:
            plt.axis('off')
            image = img_as_ubyte(clip.get_frame(index * 1. / clip.fps))
            io.imsave(imagename1,image)

            if np.ndim(image) > 2:
                h, w, nc = np.shape(image)
            else:
                h, w = np.shape(image)

            plt.figure(frameon=False, figsize=(w * 1. / 100, h * 1. / 100))
            plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
            plt.imshow(image)
            for bpindex, bp in enumerate(bodyparts2plot):
                if Dataframe[scorer][bp]['likelihood'].values[index] > pcutoff:
                    plt.plot(
                        Dataframe[scorer][bp]['x'].values[index],
                        Dataframe[scorer][bp]['y'].values[index],'.',
                        color=colors(bpindex),
                        ms=dotsize,
                        alpha=alphavalue)

            plt.xlim(0, w)
            plt.ylim(0, h)
            plt.axis('off')
            plt.subplots_adjust(
                left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
            plt.gca().invert_yaxis()
            plt.savefig(imagename2)
            plt.close("all")

def refine_labels(config,Screens=1,scale_w=.8,scale_h=.9, winHack=1, img_scale=.0076):
    """
    Refines the labels of the outlier frames extracted from the analyzed videos.\n Helps in augmenting the training dataset.
    Use the function ``analyze_video`` to analyze a video and extracts the outlier frames using the function
    ``extract_outlier_frames`` before refining the labels.

    Parameters
    ----------
    config : string
        Full path of the config.yaml file as a string.

    Screens : int value of the number of Screens in landscape mode, i.e. if you have 2 screens, enter 2. Default is 1. 
    
    scale_h & scale_w : you can modify how much of the screen the GUI should occupy. The default is .9 and .8, respectively.
   
    img_scale : if you want to make the plot of the frame larger, consider changing this to .008 or more. Be careful though, too large and you will not see the buttons fully!

    Examples
    --------
    >>> deeplabcut.refine_labels('/analysis/project/reaching-task/config.yaml', Screens=2, imag_scale=.0075)
    --------

    """
    wd = Path(config).resolve().parents[0]
    os.chdir(str(wd))
    from deeplabcut.refine_training_dataset import refinement
    refinement.show(config,Screens,scale_w,scale_h, winHack, img_scale)

def merge_datasets(config,forceiterate=None):
    """
    Checks if the original training dataset can be merged with the newly refined training dataset. To do so it will check
    if the frames in all extracted video sets were relabeled. If this is the case then the iterate variable is advanced by 1.

    Parameter
    ----------
    config : string
        Full path of the config.yaml file as a string.

    forceiterate: int, optional
        If an integer is given the iteration variable is set to this value (this is only done if all datasets were labeled or refined)

    Example
    --------
    >>> deeplabcut.merge_datasets('/analysis/project/reaching-task/config.yaml')
    --------
    """
    import yaml
    cfg = auxiliaryfunctions.read_config(config)
    config_path = Path(config).parents[0]

    bf=Path(str(config_path/'labeled-data'))
    allfolders = [os.path.join(bf,fn) for fn in os.listdir(bf) if "_labeled" not in fn] #exclude labeled data folders!
    flagged=False
    for findex,folder in enumerate(allfolders): 
        if os.path.isfile(os.path.join(folder,'MachineLabelsRefine.h5')): #Folder that was manually refine...
            pass
        elif os.path.isfile(os.path.join(folder,'CollectedData_'+cfg['scorer']+'.h5')): #Folder that contains human data set...
            pass
        else:
            print("The following folder was not manually refined,...",folder)
            flagged=True
            pass #this folder does not contain a MachineLabelsRefine file (not updated...)

    if flagged==False:
        # updates iteration by 1
        iter_prev=cfg['iteration']
        if not forceiterate:
            cfg['iteration']=int(iter_prev+1)
        else:
            cfg['iteration']=forceiterate

        with open(str(config), 'w') as ymlfile:
            yaml.dump(cfg, ymlfile,default_flow_style=False)

        print("Merged data sets and updated refinement iteration to "+str(cfg['iteration'])+".")
        print("Now you can create a new training set for the expanded annotated images (use create_training_dataset).")
    else:
        print("Please label, or remove the un-corrected folders.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config')
    parser.add_argument('videos')
    cli_args = parser.parse_args()
