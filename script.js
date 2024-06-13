function getData(){
  ajaxGetRequest('/bar', plotBar)
  ajaxGetRequest('/pi', plotPi)
}

function plotBar(response){
  let data = JSON.parse(response)
  Plotly.newPlot("barGraph", data, {title: "Incidents By Date", xaxis:{title: "Year"}, yaxis:{title:"# of Incidents"}})
}
function plotPi(response){
  let data = JSON.parse(response)
  Plotly.newPlot("piGraph", data, {title: "Incident By Day Of Week"})
}

function plotLine(response){
  let hour = document.getElementById("textbox").value
  let data = JSON.parse(response)
  Plotly.newPlot("lineGraph", data, {title: "# Of Incidents at hour " + hour, xaxis:{title: "Year"}, yaxis:{title:"# of Incidents"}})
}

function getHourData(){
  let hour = document.getElementById("textbox").value
  console.log(hour)
  ajaxPostRequest('/line', hour, plotLine)
}