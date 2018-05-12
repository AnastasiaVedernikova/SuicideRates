

let width = 1200;
let height = 600;

let colorScheme = d3.schemeReds[5];
colorScheme.unshift("#eee");
let colorScale = d3.scaleThreshold()
    .domain([1, 6, 11, 26, 101])
    .range(colorScheme);

function draw_map(data) {
    if (d3.select("svg")) {
        d3.select("svg").remove();
    }
    let projection = d3.geoNaturalEarth()
        .scale(width / 2 / Math.PI)
        .translate([width / 2, height / 2])

    let svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    let path = d3.geoPath()
        .projection(projection);

    // Data and color scale
    let map = d3.map();

    // Legend
    let g = svg.append("g")
        .attr("class", "legendThreshold")
        .attr("transform", "translate(20,20)");
    g.append("text")
        .attr("class", "caption")
        .attr("x", 0)
        .attr("y", -6)
        .text("Age-standardized suicide rates");
    let labels = ['no data', 'not applicable', '0-4.9', '5-9.9', '10-14.9', '>15'];
    let legend = d3.legendColor()
        .labels(function (d) {
            return labels[d.i];
        })
        .shapePadding(4)
        .scale(colorScale);
    svg.select(".legendThreshold")
        .call(legend);

    d3.queue()
        .defer(d3.json, "data/world.json")
        .defer(d3.csv, data, function (d) {
            map.set(d.country, +d.rate);
        })
        .await(ready);

    function ready(error, topology) {
        if (error) throw error;

        // Draw the map
        g.selectAll("path")
            .data(topojson.object(topology, topology.objects.countries).geometries)
            .enter()
            .append("path")

            .attr("fill", function (map_item) {
                // Pull data for this country
                map_item.rate = map.get(map_item.properties.name) || 0;
                // Set the color
                return colorScale(map_item.rate);
            })
            .attr("d", path);

    }

}

// Load external data and boot
document.querySelector(".button_2010").addEventListener("click", function (){
    draw_map("data/both_sexes_2010_data.csv");
});
document.querySelector(".button_2015").addEventListener("click", function (){
    draw_map("data/both_sexes_2015_data.csv");
});
document.querySelector(".button_2005").addEventListener("click", function (){
    draw_map("data/both_sexes_2005_data.csv");
});
document.querySelector(".button_2000").addEventListener("click", function (){
    draw_map("data/both_sexes_2000_data.csv");
});
