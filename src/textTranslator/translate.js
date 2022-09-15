

function Display(x) 
{
    const exec = require('child_process').exec;
    const script = exec('python', ['./arrenmentString.py']);
    // string
    const data_to_pass_in = x;
    console.log(" Data sent to python script : ", data_to_pass_in);
    script.stdout.on('data', (data) => {
        console.log('Data received from python script :', data.toString())
        document.getElementById("textTrans").innerText = data.toString()
    })
}
Display("hello") 