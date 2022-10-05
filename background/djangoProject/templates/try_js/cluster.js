    data_points=[]

    function object2Geojson(data) {
        //坐标数组 [{},{}] 转geojson
        var featureCollection = { "type": "FeatureCollection" };
    	var features = new Array();

    	for (let i = 0; i < data.length; i++) {
    	var feature = { "type": "Feature" };
    	feature.properties = data[i];
    	var geometry = { "type": "Point" };
    	geometry.coordinates = [data[i].LON, data[i].LAT];
    	feature.geometry = geometry;
    	features.push(feature);
    	}

    	featureCollection.features = features;
    	return featureCollection;
    }

    function func_cluster(data) {
        var options = {numberOfClusters: 4};
        var clustered = turf.clustersKmeans(object2Geojson(data), options);
        return clustered
    }

    function func_cluster_try(){
                $.ajax({
                url: '/api_stay_points_return/',
                type: 'GET',
                dataType: 'json',
                data: {'id': 1, 'dist_th': 200 ,'time_th':500},
                success: function (dat) {
                    var jsonData = JSON.stringify(dat);// 转成JSON格式
                    alert(jsonData);

                    var count_points=dat.result.count
                    for(var i=0;i<count_points;i++) {
                        var lat_i = dat.result.data[i].points[0].lat
                        var lng_i = dat.result.data[i].points[0].lng
                        data_points.push(
                            {
                                'LON':lat_i,
                                'LAT':lng_i,
                            }
                        )
                    }
                    clu=func_cluster(data_points)
                    //data_points=[{'LAT':xx,'LNG':xx},{},{}]
                }
            }
        )

    }
