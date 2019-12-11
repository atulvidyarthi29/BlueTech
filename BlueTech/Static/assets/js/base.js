let myVar;

function myFunction() {
    myVar = setTimeout(showPage, 500);
}

function showPage() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("style-main").style.display = "block";
}


// var modalTinyNoFooter = new tingle.modal({
//     onClose: function () {
//         console.log('close');
//     },
//     onOpen: function () {
//         console.log('open');
//     },
//     beforeOpen: function () {
//         console.log('before open');
//     },
//     beforeClose: function () {
//         console.log('before close');
//         return true;
//     },
//     cssClass: ['class1', 'class2']
// });
// var btn = document.querySelector('.js-tingle-modal-1');
// btn.addEventListener('click', function () {
//     modalTinyNoFooter.open();
// });
// modalTinyNoFooter.setContent(document.querySelector('.tingle-demo-tiny').innerHTML);
//
