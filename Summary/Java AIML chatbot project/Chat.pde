
void createChatSession() {
  botter = new Bot("super", dataPath(""));
  chatSession = new Chat(botter);
}

void sendToBot(String message) {
  String response = chatSession.multisentenceRespond(message);
  display(response, message);
}

void display(String robot, String human) {
  
  if (counter > 631){
    background(255);
    counter = 30;
  }
  String format_hum = "Me: " + human;
  String format_rob = "Bot: " + robot;
  textSize(20);
  fill(0, 0, 0);
  text(format_hum,  20, 30 + counter);
  textSize(20);
  fill(0,0,255);
  text(format_rob, 20, 60 + counter);
}
