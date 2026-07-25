const messages = document.getElementById("messages");
const input = document.getElementById("input");


document.getElementById("plugins").innerText =
"Plugin System Ready";



function sendMessage(){

    let text = input.value;


    if(text === "") return;


    addMessage(
        "You: " + text
    );


    let response =
    generateResponse(text);


    setTimeout(()=>{

        addMessage(
            "Alfred: " + response
        );

    },500);


    input.value="";

}



function addMessage(text){

    let div =
    document.createElement("div");


    div.className="message";

    div.innerText=text;


    messages.appendChild(div);

}



function generateResponse(message){

    message =
    message.toLowerCase();


    if(message.includes("hello")){

        return "Hello. Alfred is online.";

    }


    if(message.includes("status")){

        return "All systems are operational.";

    }


    if(message.includes("name")){

        return "I am Alfred.";

    }


    return "I am still learning this command.";

}
