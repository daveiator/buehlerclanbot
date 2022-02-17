import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public class Gamemanager {


    private MyListener listener;
    private MessageReceivedEvent event;
    private Game[] allGames;

    public Gamemanager() {
    }

    public Gamemanager(MyListener initListener) {
        this.listener = initListener;
    }

    public void receiveEvent(MessageReceivedEvent initEvent) {
        this.event = initEvent;
        System.out.println("Event received by Gamemangager!");
        command();


    }
    public void printMessage(String message) {

    }


    private void command() {
        String message;
        String lcmessage;
        MessageChannel leChannel = event.getChannel();
            message = event.getMessage().getContentRaw();
        lcmessage = message.toLowerCase();
        System.out.println("Game-Message is:" + message + " / "+ lcmessage);

        switch (lcmessage) {
            case "games":
                //List all games
                String output = "Aveilable games:\n";
                for (int i = 0; i < allGames.length; i++) {
                    output = String.join("\n▫",allGames[i].getName());

            }
        }
    }
    public void createSession() {

    }

    public void init() {
    }
}
