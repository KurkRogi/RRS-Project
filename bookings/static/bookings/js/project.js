// Close messages after 3s
window.setTimeout(closeMessageBox, 3000);
function closeMessageBox() {
    var messageBox = document.getElementById('message-box');
    if (messageBox) {
        messageBox = new bootstrap.Alert(messageBox);
        messageBox.close();
        messageBox.parentElement.remove();
    }
}