#!/usr/bin/bash
cd conda.recipe
conda build .
cd ..
if [ !-d "build" ] then
    mkdir build
fi
conda create -p ./0.0.3 -c ~/anaconda3/conda-bld/noarch pygarth