#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from  PhysicsTools.NanoAODTools.postprocessing.examples.exampleModule import *
from  PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
p=PostProcessor(".",inputFiles(),"Jet_pt>200",modules=[exampleModule(), puWeight()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
p.run()

print "DONE"
os.system("ls -lR")

