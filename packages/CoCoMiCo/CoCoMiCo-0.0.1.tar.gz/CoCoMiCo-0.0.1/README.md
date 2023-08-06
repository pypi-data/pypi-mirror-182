# CoCoMiCo : COoperation and COmpetition in MIcrobial COmmunities

CoCoMiCo is a python3 tool
aims at comparing and selecting communities based on their cooperation and competition potentials. 
# How to use it ?

## input

The packages 


The script takes a folder containing sub-folders as input. the SBML and community sub-folders correspond respectively to metabolic network in SBML format and a list of bacterial community of size x in json format. 

```
Folder_input
├── community
│   └── Folder_input_size_x.json
|    ..
├── sbml
│   └── species_1.sbml
│   └── species_4.sbml
|    ..
```

## Exemple of execution

`
python B2B/src/pipeline.py community_samples -json_com B2B -seed_path common_seed.sbml -sampling 150  -metrics all -ecosystem root_
`


