// WebSocket connect
// let url = `ws://${window.location.host}/ws/socket-server/`

// const chatSocket = new WebSocket(url)

// chatSocket.onmessage = function(e) {
//     let data = JSON.parse(e.data)
//     console.log('Data:', data)
// }




// 1. Ajax xRequests to API
let url = `http://${window.location.host}/api/chatroom/`

// XML METHOD
let xhr = new XMLHttpRequest();
xhr.open('get', url, true);
xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
        // console.log(xhr)
        console.log(JSON.parse(xhr.responseText))
        const chatRoomsJson = JSON.parse(xhr.responseText)
        createChatRoomsDivsByJSON(chatRoomsJson)

        console.log(chatRoomsDiv)
    }    
}
xhr.send()




// 2. Create ChatRoomDivs
const chatRoomsDiv = document.getElementById('chatrooms')

function createChatRoomsDivsByJSON(chatRoomsJson) {
    chatRoomsJson.forEach(chatRoomJson => {
        chatRoomsDiv.appendChild(createChatRoomDiv(chatRoomJson)) 
    });  
};















// 3. создание компонентов для страницы
// TODO: Создавать див class='message_div ?mark as read' с id='chatroom_ID' 
function createChatRoomDiv(chatRoomJson) {
    let chatRoomId = chatRoomJson.id
    const div = document.createElement('div');
    div.classList.add(`messege_div`);
    div.setAttribute('id', chatRoomId)
    // div.classList.add(`roomid_${chatRoomId}`);
    div.innerHTML = `<div class="messege_div_title">
                        <img class="messege_div_avatar" src='avatar_img'{% static "mainApp/img/medium.jpg" %} alt="avatar">
                        <div class="user_info">
                            <p>nickname</p>
                            <p class="mes">message chatroom id - ${chatRoomId}</p>
                        </div>  
                        <div class="messege_info">
                            <p class="date">date time</p>
                        </div>
                    </div>`
    return div
    }









function createDialogDiv() {}

function createMessageDiv() {}









// TODO: Сделать модель чата, из которой будут строиться все отображение