function sendKeyCombo(keyCombo) {

    let request = {
        method: "POST",
        body: JSON.stringify({"keyCombo": keyCombo}),
        headers: {"Content-Type": "application/json"},
        mode: "cors"
    };
    fetch("http://localhost:5000/keycombination", request).then(a => a.text()).then(b=> console.log(JSON.parse(b)));
}