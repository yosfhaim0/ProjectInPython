
const fs = require("fs");
fs.readFile("commonWordsEnglish.txt", (err, data) => {
    if (err) throw err;

    console.log(data.toString());
});



function translateMyText(){
    const text=document.getElementById("textUnTrans").value
    const arr=text.split(" ")
    const tratex=turnArrStringToTextWhitTranslate(arr)
    document.getElementById("translateText").innerText=tratex

}

function findIfInCommon(common, arstrElement) {
    return false;
}

function turnArrStringToTextWhitTranslate(x)
{
    var twt=""
    let fiallr = new Set();
    var numOfTra=0
    try {
        x.forEach(element => {
            twt+=element
            if(!(fiallr.has(element))){
                const regex =new RegExp('\b[A-Za-z_|\'|\-]+\b')
                var arstr=element.match(regex)
                if(arstr && arstr[0].charAt(0).toUpperCase() && arstr[0].length() > 2 &&  findIfInCommon(commonLeval2, arstr[0]) &&  findIfInCommon(commonLeval2, arstr[0])){
                    const translate=traslate_word(arstr[0])
                    if(translate && !element===translate && translate.length > 2){
                        twt += "= " + translate.toString()
                        findAllReady.add(i)
                        numOfTra+=1
                    }
                }
            }
            twt += " "
        });

    }
    finally {
        console.log("num Of Translate word : ",numOfTra)
    }
    return twt
}
