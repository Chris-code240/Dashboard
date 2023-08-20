var dropDowns = document.querySelectorAll('.dropdown')
dropDowns.forEach(ele=>{
ele.addEventListener('click',()=>{
    ele.lastElementChild.classList.toggle('fa-chevron-down')
    ele.lastElementChild.classList.toggle('fa-chevron-up')
    ele.parentElement.parentElement.querySelector('.drop-menu').classList.toggle('hidden')
})
})

console.log("Side")