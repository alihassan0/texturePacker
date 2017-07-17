- names shouldn't have "." but in their extension
- how many frames the spritesheet have should be encoded in the file names 
```
x = number of frames in row
y = number of frames in column
fileName = "imageName_x_y.format"
```
## Done
- you can supply paths to the script and it will an output with that file 
```
python texturePack.py assets/draftKnight
```
`@NOTE` don't add / at the end of path
- remove opencv dependency

## RoadMap 
- remove 
- make it trim using transperent values instad of black values 
- trim resulting texture Atlass