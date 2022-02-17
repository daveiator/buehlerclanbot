import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;


public class MyListener extends ListenerAdapter {

    private Gamemanager gamemanager = new Gamemanager(this);

    private boolean listening = true;   //<- Enable listening
    private boolean prefixEnable = true;    //<- Enable prefix
    private String prefix = "!";    //<- Set prefix

    private String gameChannel = "747097612800360508";  //<- Set game channel ID

    //Init (Gets called before bot is build)
    public void init() {

    }

    //Check all messages
    @Override
    public void onMessageReceived(MessageReceivedEvent event)
    {
        if (event.getAuthor().isBot()) return;  //Don't respond to bots

        //Console log
        System.out.println("Received Message!");
        System.out.println(event.getAuthor().getName() + " says: " + event.getMessage().getContentDisplay() + " in Channel: "+ event.getChannel().getName());

        //Send game channel messages to the Game-Manager
        if(event.getChannel().getId().equals(gameChannel)) {
            gamemanager.receiveEvent(event);
        }

        else if ((listening && event.getMessage().getContentRaw().startsWith(prefix) && prefixEnable) || listening && !prefixEnable) {
            command(event);
        }

    }
    //Analyse messages
    public void command(MessageReceivedEvent leEvent) {
        String message;
        String lcmessage;
        MessageChannel leChannel = leEvent.getChannel();
        if(prefixEnable) {
             message = leEvent.getMessage().getContentRaw().replaceFirst(prefix,"");    //Remove prefix from message
        } else {
            message = leEvent.getMessage().getContentRaw();
        }
        lcmessage = message.toLowerCase();  //Create message in lower case

        System.out.println("Message is:" + message + " / "+ lcmessage); //Console log

        if (lcmessage.startsWith("mock ")) {
            //mock
            leChannel.sendMessage((mock(lcmessage.replaceFirst("mock ", "")))).queue();
            return;
        } else if (lcmessage.startsWith("repeat ")) {
            //repeat
            leChannel.sendMessage(message.replaceFirst("repeat ", "")).queue();
            return;
        }
        switch (lcmessage) {
            case "do a flip":
                //do a flip
                leChannel.sendMessage("Flip!").queue();
                break;

            case "good bot":
                //good bot
                leChannel.addReactionById(leEvent.getMessageId(),"U+1F60A").queue();
                break;

            case "bad bot":
                //bad bot
                leChannel.sendMessage("https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Ffacebook%2F000%2F031%2F856%2Fig11.jpg").queue();
                break;

            case "meow woem":
                //meow woem
                leChannel.sendMessage("https://media.discordapp.net/attachments/736362433634893924/746391689123594341/image0-5-2.gif").queue();
                leChannel.sendMessage("https://media.discordapp.net/attachments/736362433634893924/746391689421258912/image0-3-1.gif").queue();
                break;



                //TODO /\ Add more commands /\

            default:
                //Default error message
                leChannel.sendMessage("You picked the wrong command, fool!").queue();

        }
    }

    //Small Command- funcions
    public String mock(String input) {
        //Mocking code by Schmierstoff
        String output = "";
         for(int i=0;i<input.length();i++) {
             boolean upper = Math.random() < 0.5;
             String letter = input.substring(i, i + 1);
             if (letter.matches("[a-zA-Z]")) {
                 if (upper) letter = letter.toUpperCase();
                 else letter = letter.toLowerCase();
                 output = output.concat(letter);
             } else output = output.concat(letter);
         }
         return output;
    }

    //Get- & Set functions

    public boolean isListening() {
        return listening;
    }
    public boolean isPrefixEnable() {
        return prefixEnable;
    }
    public String getPrefix() {
        return prefix;
    }
}
