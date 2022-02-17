import net.dv8tion.jda.api.AccountType;
import net.dv8tion.jda.api.JDABuilder;


import javax.security.auth.login.LoginException;

public class Main {

    public static void main (String args[]) throws LoginException {

        MyListener listener = new MyListener();
        //Call init
        listener.init();
        //Create bot
        JDABuilder builder = new JDABuilder(AccountType.BOT);
        String token = ""; //<--Insert bot token
        builder.setToken(token);
        builder.addEventListeners(listener);
        builder.build();    //Build bot
        System.out.println("Build finished!");

    }
}
