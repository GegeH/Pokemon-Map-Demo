var map;
function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
        credentials: 'Ahx-pu4sUrSfP72S4B7gtzvf_FB6JV5OTgJazEna5ZQ7QFm67ATaqUI3K-KSLtxz'
    });
}

// 1. Define pokemon data format, create mock pokemon data
map_items = [
    {
        "pokemon_id" : 12,
        "expire" : 1234567,
        "longitude" : -73.9828028,
        "latitude" : 40.7575988
    }
]

// 2. Create pokemon image on map
function get_pokemon_layer_from_map_itmes(map_items) {
    var pushpins = Microsoft.Maps.TestDataGenerator.getPushpins(10, map.getBounds());
    var layer = new Microsoft.Maps.Layer();
    return layer;
}
    

var pokemon_layer = get_pokemon_layer_from_map_itmes(map_items)
layer.add(pushpins);
map.layers.insert(layer);
    
    
// 3. Add pokemon counter down refresh

// 4. Connect with REST API
