import interfascia.*;
import org.alicebot.ab.Chat;
import org.alicebot.ab.History;
import org.alicebot.ab.MagicBooleans;
import org.alicebot.ab.MagicStrings;
import org.alicebot.ab.utils.IOUtils;
GUIController c;
Bot botter;
Chat chatSession;
IFTextField t;
public static int counter;
void setup() {
  size(1000, 800);
  background(255);
  
  textSize(28);
  
  fill(0, 0, 0);
  text("Welcome to our Restaurant!", 370, 200);
  text("Make your booking below by telling the chat bot you would like to make a booking.", 20, 300);
  
  
  c = new GUIController (this);
 
  t = new IFTextField("Input", 0, 700, 1000);
  c.add(t);
  t.addActionListener(this);
  
  
  
}

void draw() {
  
  createChatSession();
  
}


void actionPerformed(GUIEvent e) {
  
  if (e.getMessage().equals("Completed")) {
    if (counter == 0){
    background(255);
    counter = counter + 30;
    String userMessage = t.getValue();
    t.setValue("");
    sendToBot(userMessage);
    }
    else {
      counter = counter + 60;
      String userMessage = t.getValue();
      t.setValue("");
      sendToBot(userMessage);
    
    }
  }
  }
