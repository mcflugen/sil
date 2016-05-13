#    #### Manual Flags, to be applied to WAIS as a concatenated file, left here for SPIce    
#    if verbose == 0:     #For crunching individual files and pruning by indices #### Can change to 0 FOR PROBLEM FILES through batch crunch
#        startpflag = input("Please input start indices for data to be flagged for TAILS IN OR OUT of unknown reasons, in [ ], for p flag") 
#        endpflag = input("Please input end indices for data to be flagged for TAILS IN OR OUT of unknown reasons, in [ ], for p flag") 
#        if len(startpflag) >= 1:
#            flagindex = np.arange(len(startpflag))
#            for f in flagindex:
#                findex = np.arange(startpflag[f],endpflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'p'
#        startsflag = input("Please input start indices for data to be flagged for SPIKES of unknown reasons, in [ ], for s flag") 
#        endsflag = input("Please input end indices for data to be flagged for SPIKES of unknown reasons, in [ ], for s flag") 
#        if len(startsflag) >= 1:
#            flagindex = np.arange(len(startsflag))
#            for f in flagindex:
#                findex = np.arange(startsflag[f],endsflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'s'
#        startnflag = input("Please input start indices for data to be flagged for NOISE of unknown reasons, in [ ], for n flag") 
#        endnflag = input("Please input end indices for data to be flagged for NOISE of unknown reasons, in [ ], for n flag") 
#        if len(startnflag) >= 1:
#            flagindex = np.arange(len(startnflag))
#            for f in flagindex:
#                findex = np.arange(startnflag[f],endnflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'n'
#        startoflag = input("Please input start indices for data to be flagged for OUTLIERS of unknown reasons, in [ ], for o flag") 
#        endoflag = input("Please input end indices for data to be flagged for OUTLIERS of unknown reasons, in [ ], for o flag") 
#        if len(startoflag) >= 1:
#            flagindex = np.arange(len(startoflag))
#            for f in flagindex:
#                findex = np.arange(startoflag[f],endoflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'o'
#        startvflag = input("Please input start indices for data to be flagged for VALCO reasons, in [ ], for v flag") 
#        endvflag = input("Please input end indices for data to be flagged for VALCO reasons, in [ ], for v flag") 
#        if len(startvflag) >= 1:
#            flagindex = np.arange(len(startvflag))
#            for f in flagindex:
#                findex = np.arange(startvflag[f],endvflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'v'
#        startfflag = input("Please input start indices for data to be flagged for FILTER CHANGE reasons, in [ ], for f flag") 
#        endfflag = input("Please input end indices for data to be flagged for FILTER CHANGE reasons, in [ ], for f flag") 
#        if len(startfflag) >= 1:
#            flagindex = np.arange(len(startfflag))
#            for f in flagindex:
#                findex = np.arange(startfflag[f],endfflag[f])
#                for l in findex:
#                    icedata_dict["flag3"][l] = icedata_dict["flag3"][l]+'f'
