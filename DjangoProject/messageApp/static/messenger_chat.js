// WebSocket connect
// let url = `ws://${window.location.host}/ws/socket-server/`

// const chatSocket = new WebSocket(url)

// chatSocket.onmessage = function(e) {
//     let data = JSON.parse(e.data)
//     console.log('Data:', data)
// }







function chooseInterlocutor(chatRoomJson, requester_id) {
    if (requester_id == chatRoomJson.creater.id) {
        return chatRoomJson.interlocutor
    } else if (requester_id == chatRoomJson.interlocutor.id) {
        return chatRoomJson.creater
    }
}

function getFullUrlWithHost(url) {
    return `http://${window.location.host}${url}`
}

// 3. создание компонентов для страницы
function createChatRoomDiv(chatRoomJson, requester_id) {
    let chatRoomId = chatRoomJson.id
    // Выбор кого отображать собеседником для chatRoom 
    let interlocutor = chooseInterlocutor(chatRoomJson, requester_id)
    let interlocutorAvatar = getFullUrlWithHost(interlocutor.avatar)
    

    const div = document.createElement('form');
    div.classList.add(`messege_div`);
    div.setAttribute('id', `chatRoomId${chatRoomId}`)

    // TEST TEST TEST TEST TEST TEST
    // TEST TEST TEST TEST TEST TEST
    


    
    // TEST TEST TEST TEST TEST TEST
    // TEST TEST TEST TEST TEST TEST



    // div.classList.add(`roomid_${chatRoomId}`);
    div.innerHTML = `<div class="messege_div_title">
                        <img class="messege_div_avatar" src='${interlocutorAvatar}' alt="avatar">
                        <div class="user_info">
                            <p>${interlocutor.username}</p>
                            <p class="mes">??last message chatroom id - ${chatRoomId}</p>
                        </div>  
                        <div class="messege_info">
                            <p class="date">??last message datetime</p>
                            <div class="read_or">
                                ??<i></i><i></i>
                            </div>
                        </div>
                    </div>`
    div.onclick = function () {
        // delat ajax запрос по chatroomid
        alert('вы напугали деда')
    }
    return div
    }

















// TODO: Сделать модель чата, из которой будут строиться все отображение


// ОБЪЕКТ CHATROOMS
var chatRoomsModer = function () {
    const chatRoomsDiv = document.getElementById('chatrooms')
    return {
        div: chatRoomsDiv,
        stateNull: () => {chatRoomsDiv.innerHTML = `<span class='empty_chatrooms'>Загрузка</span>`},
        state0: () => {chatRoomsDiv.innerHTML = `<span class='empty_chatrooms'>У вас нет чатов</span>`},
        state1: (chatRoomsJson, requester_id) => {
            // Обнуление
            chatRoomsDiv.innerHTML = ''
            // Добавление
            chatRoomsJson.forEach(chatRoomJson => {
                chatRoomsDiv.appendChild(createChatRoomDiv(chatRoomJson, requester_id)) 
            });
        }
    }
}




// ОБЪЕКТ CHATFORM
var chatModer = function () {
    const chatDiv = document.getElementById('chatDiv')

    return {
        stateNull: () => {chatDiv.innerHTML = `<button class="chat_brg" id="burger_chat"> 
                                                    <div></div>
                                                    <div></div>
                                                    <div></div>
                                                </button>
                                                <span class='empty_messanger'></span>`},
        createFrom: () => {}
    }
}














// 1. Ajax xRequests to API
let url = `http://${window.location.host}/api/chatroom/`

// XML METHOD
let xhr = new XMLHttpRequest();
xhr.open('get', url, true);
xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
        // console.log(xhr)
        console.log('xhr response.json - ', JSON.parse(xhr.responseText))
        let jsonData = JSON.parse(xhr.responseText)

        const Rooms = chatRoomsModer()
        const Chat = chatModer()
        if (jsonData.data.length > 0) {
            Rooms.state1(jsonData.data, jsonData.requester_id)
            console.log('div - ', Rooms.div)
        } else {
            Rooms.state0()
        }

    }    
}
xhr.send()



