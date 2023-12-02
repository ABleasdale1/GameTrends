function switchView(view) {
    var contents = document.getElementsByClassName('content');
    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    document.getElementById(view).style.display = 'block';
}

function showEditForm() {
    document.getElementById('editForm').style.display = 'block';
}