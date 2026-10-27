// This file contains material supporting section 3.7 of the textbook:
// "Object Oriented Software Engineering" and is issued under the open-source
// license found at www.lloseng.com 

package client;

import ocsf.client.*;
import common.*;
import java.io.*;

/**
 * This class overrides some of the methods defined in the abstract
 * superclass in order to give more functionality to the client.
 *
 * @author Dr Timothy C. Lethbridge
 * @author Dr Robert Lagani&egrave;
 * @author Fran&ccedil;ois B&eacute;langer
 * @version July 2000
 */
public class ChatClient extends AbstractClient
{
  //Instance variables **********************************************
  
  /**
   * The interface type variable.  It allows the implementation of 
   * the display method in the client.
   */
  ChatIF clientUI; 

  
  //Constructors ****************************************************
  
  /**
   * Constructs an instance of the chat client.
   *
   * @param host The server to connect to.
   * @param port The port number to connect on.
   * @param clientUI The interface type variable.
   */
  
  public ChatClient(String host, int port, ChatIF clientUI) 
    throws IOException 
  {
    super(host, port); //Call the superclass constructor
    this.clientUI = clientUI;
    openConnection();
  }

  
  //Instance methods ************************************************
    
  /**
   * This method handles all data that comes in from the server.
   *
   * @param msg The message from the server.
   */
  public void handleMessageFromServer(Object msg) 
  {
    clientUI.display(msg.toString());
  }

  @Override
protected void connectionException(Exception exception)
{
  clientUI.display(
    "Serverul s-a oprit sau conexiunea s-a pierdut. Clientul se inchide.");
  quit();
}

  /**
   * This method handles all data coming from the UI            
   *
   * @param message The message from the UI.    
   */

  private void handleCommand(String message)
{
  String[] parts = message.trim().split("\\s+");
  String command = parts[0];

  // Verificam cate argumente trebuie sa aiba comanda.
  int expectedParts =
      (command.equals("#sethost") || command.equals("#setport")) ? 2 : 1;

  if (parts.length != expectedParts)
  {
    clientUI.display(
        "Argumente incorecte. Exemplu: #sethost localhost sau #setport 6000.");
    return;
  }

  try
  {
    switch (command)
    {
      case "#quit":
        quit();
        break;

      case "#logoff":
        if (!isConnected())
        {
          clientUI.display("Esti deja deconectat.");
        }
        else
        {
          closeConnection();
          clientUI.display("Te-ai deconectat. Clientul ramane pornit.");
        }
        break;

      case "#sethost":
        if (isConnected())
        {
          clientUI.display("Foloseste #logoff inainte sa schimbi hostul.");
        }
        else
        {
          setHost(parts[1]);
          clientUI.display("Host schimbat: " + getHost());
        }
        break;

      case "#setport":
        if (isConnected())
        {
          clientUI.display("Foloseste #logoff inainte sa schimbi portul.");
        }
        else
        {
          int port = Integer.parseInt(parts[1]);

          if (port < 1 || port > 65535)
          {
            clientUI.display("Portul trebuie sa fie intre 1 si 65535.");
            return;
          }

          setPort(port);
          clientUI.display("Port schimbat: " + getPort());
        }
        break;

      case "#login":
        if (isConnected())
        {
          clientUI.display("Esti deja conectat.");
        }
        else
        {
          openConnection();
          clientUI.display(
              "Conectat la " + getHost() + ":" + getPort());
        }
        break;

      case "#gethost":
        clientUI.display("Host: " + getHost());
        break;

      case "#getport":
        clientUI.display("Port: " + getPort());
        break;

      default:
        clientUI.display("Comanda necunoscuta: " + command);
        break;
    }
  }
  catch (NumberFormatException e)
  {
    clientUI.display("Portul trebuie sa fie un numar intreg.");
  }
  catch (IOException e)
  {
    clientUI.display("Operatia de conectare/deconectare a esuat.");
  }
}


  public void handleMessageFromClientUI(String message)
{
  if (message == null)
  {
    quit();
    return;
  }

  if (message.startsWith("#"))
  {
    handleCommand(message);
    return;
  }

  if (!isConnected())
  {
    clientUI.display("Esti deconectat. Foloseste #login.");
    return;
  }

  try
  {
    sendToServer(message);
  }
  catch (IOException e)
  {
    clientUI.display("Mesajul nu a putut fi trimis.");
  }
}
  
  /**
   * This method terminates the client.
   */
  public void quit()
  {
    try
    {
      closeConnection();
    }
    catch(IOException e) {}
    System.exit(0);
  }
}
//End of ChatClient class
