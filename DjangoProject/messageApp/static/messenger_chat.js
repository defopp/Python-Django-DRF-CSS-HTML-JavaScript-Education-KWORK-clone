// WebSocket connect
// let url = `ws://${window.location.host}/ws/socket-server/`

// const chatSocket = new WebSocket(url)

// chatSocket.onmessage = function(e) {
//     let data = JSON.parse(e.data)
//     console.log('Data:', data)
// }


// создание компонентов для страницы
function getChatRoomDiv() {}

function getDialogDiv() {}

function getMessageDiv() {}



// Ajax xRequests to API
let url = `http://${window.location.host}/api/chatroom/`

// XML METHOD
let xhr = new XMLHttpRequest();
xhr.open('get', url, true);
xhr.onreadystatechange = function () {

    if (xhr.readyState == 4 && xhr.status == 200) {
        // console.log(xhr)
        console.log(JSON.parse(xhr.responseText))
    }

}
xhr.send()






// FETCH request METHOD
// let promise = fetch(url);
// let response = new Response(promise)

// if (response.ok) {
//     console.log('ok ', response)
// }


