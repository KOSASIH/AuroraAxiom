// src/frontend/script.js
import * as tf from "@tensorflow/tfjs";
import * as Plotly from "plotly.js";

const predictBtn = document.getElementById("predict-btn");
const preventBtn = document.getElementById("prevent-btn");
const mitigateBtn = document.getElementById("mitigate-btn");
const visualizeBtn = document.getElementById("visualize-btn");
const resultDiv = document.getElementById("result");
const plotDiv = document.getElementById("plot");

predictBtn.addEventListener("click", async () => {
    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ /* input data */ }),
    });
    const result = await response.json();
    resultDiv.innerText = `Predicted disaster: ${result.prediction}`;
});

preventBtn.addEventListener("click", async () => {
    const response = await fetch("/prevent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ /* input data */ }),
    });
    const result = await response.json();
    resultDiv.innerText = `Prevention measures: ${result.prevention_measures}`;
});

mitigateBtn.addEventListener("click", async () => {
    const response = await fetch("/mitigate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ /* input data */ }),
    });
    const result = await response.json();
    resultDiv.innerText = `Mitigation measures: ${result.mitigation_measures}`;
});

visualizeBtn.addEventListener("click", async () => {
    const response = await fetch("/visualize", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });
    const data = await response.json();
    const plotData = [
        {
            x: data.labels,
            y: data.values,
            type: "bar",
        },
    ];
    Plotly.newPlot(plotDiv, plotData);
});