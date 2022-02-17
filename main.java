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
        String token = "NzQ1NzM4NTI3NzAyMTIyNTM2.Xz2JIA.TyNmFfcLtMb8nHn4nrKQowhUo5Q"; //<--Insert bot token
        builder.setToken(token);
        builder.addEventListeners(listener);
        builder.build();    //Build bot
        System.out.println("Build finished!");

    }
}
