console.log(document.querySelector('aside'))

if(!document.querySelector('aside')){
    document.querySelectorAll('.side-script').forEach(ele=>ele.remove())
    console.log("Nothing...")
}
// document.querySelector('aside')? document.body.appendChild(script) : document.querySelector('#side-script').remove()

window.onresize = ()=>{
    if(!document.querySelector('aside')){
        document.querySelectorAll('.side-script').forEach(ele=>ele.remove())
        console.log("Nothing...")
    }
}