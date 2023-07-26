# fuzzy_api
fuzzy api with flask

## Enpoint
```
POST : /processjson
```
```json
{
	"SoilWaterContent" : "23",
	"SunshineHour": "12",
	"DeltaEvaporation": "3",
	"PlantAge": "14"
}
```
```
GET : /latest-config
```
```
POST : /config-update
```
```json
{
    "params" : 
    {
        "input": 
        [
            {
                "param_name": "SoilWaterContent",
                "universe":[0, 40, 0.1],
                "membership":{
                    "Kritis": [0, 0, 26, 28],
                    "Sangat Kritis": [27, 28, 29, 30],
                    "Kurang Baik": [29, 30, 34, 35],
                    "Baik": [34, 35, 40, 40]
                }
            },
            {
                "param_name": "DeltaEvaporation",
                "universe":[0, 12, 0.1],
                "membership":{
                    "Small": [0, 0, 1, 3],
                    "Medium": [1, 3, 4, 5],
                    "Large": [3, 5, 6, 6]
                }
            },
            {
                "param_name": "SunshineHour",
                "universe":[0, 6, 0.1],
                "membership":{
                    "Short": [0, 0, 2, 6],
                    "Medium": [2, 6, 7, 10],
                    "Long": [6, 10, 12, 12]
                }
            },
            {
                "param_name": "PlantAge",
                "universe":[0, 14, 0.1],
                "membership":{
                    "Germination": [0, 0, 3, 6],
                    "Tillering": [3, 6, 8, 9],
                    "Growth": [6, 9, 10, 12],
                    "Ripening": [9, 12, 15, 15]
                }
            }
        ],
        "output":
        [
            {
                "param_name": "BobotPenyiraman",
                "universe":[0, 120, 0.1],
                "membership":{
                    "Singkat": [0, 0, 15, 30],
                    "Lama": [15, 30, 60, 75],
                    "SangatLama": [60, 75, 90, 100]
                }
            }
        ],
        "rule": 
        [
            ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], 
            ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], 
            ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], ["SangatLama"], ["SangatLama"], ["Lama"], ["SangatLama"], 
            ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], 
            ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["SangatLama"], ["Lama"], ["Singkat"], ["SangatLama"], 
            ["Lama"], ["Lama"], ["Lama"], ["Lama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], 
            ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Lama"], ["Singkat"], ["Lama"], 
            ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], 
            ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["Lama"], ["Lama"], ["Singkat"], ["Lama"], ["SangatLama"], ["Lama"], ["Lama"], ["SangatLama"], 
            ["Singkat"], ["Singkat"], ["Singkat"], ["Singkat"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], 
            ["Singkat"], ["Singkat"], ["Singkat"], ["Singkat"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], 
            ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Singkat"], ["Singkat"], ["Lama"], ["Lama"], ["Lama"], ["Singkat"], ["Lama"]
        ]
    }
}
```

## Deployment
https://medium.com/geekculture/deploying-flask-application-on-vps-linux-server-using-nginx-a1c4f8ff0010