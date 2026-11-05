import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import common.ChatIF;

/** Console interface for messages entered by the server operator. */
public class ServerConsole implements ChatIF
{
  private final EchoServer server;

  public ServerConsole(int port) throws IOException
  {
    server = new EchoServer(port, this);
    server.listen();
  }

  public void accept() throws IOException
  {
    BufferedReader console =
        new BufferedReader(new InputStreamReader(System.in));
    String message;

    while ((message = console.readLine()) != null)
    {
      server.handleMessageFromServerUI(message);
    }
  }

  @Override
  public void display(String message)
  {
    System.out.println(message);
  }

  public static void main(String[] args)
  {
    if (args.length > 1)
    {
      System.out.println("Utilizare: java ServerConsole [port]");
      return;
    }

    int port = EchoServer.DEFAULT_PORT;
    try
    {
      if (args.length == 1)
      {
        port = Integer.parseInt(args[0]);
      }
      if (port < 1 || port > 65535)
      {
        System.out.println("Portul trebuie sa fie intre 1 si 65535.");
        return;
      }
    }
    catch (NumberFormatException e)
    {
      System.out.println("Portul trebuie sa fie un numar intreg.");
      return;
    }

    ServerConsole console = null;
    try
    {
      console = new ServerConsole(port);
      console.accept();
    }
    catch (IOException e)
    {
      System.out.println("Eroare server: " + e.getMessage());
    }
    finally
    {
      if (console != null)
      {
        try
        {
          console.server.close();
        }
        catch (IOException e)
        {
          console.display("Eroare la inchiderea serverului: " + e.getMessage());
        }
      }
    }
  }
}
