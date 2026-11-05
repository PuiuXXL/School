// This file contains material supporting section 3.7 of the textbook:
// "Object Oriented Software Engineering" and is issued under the open-source
// license found at www.lloseng.com 

import java.io.*;
import ocsf.server.*;
import common.ChatIF;

/**
 * This class overrides some of the methods in the abstract 
 * superclass in order to give more functionality to the server.
 *
 * @author Dr Timothy C. Lethbridge
 * @author Dr Robert Lagani&egrave;re
 * @author Fran&ccedil;ois B&eacute;langer
 * @author Paul Holden
 * @version July 2000
 */
public class EchoServer extends AbstractServer 
{
  //Class variables *************************************************
  
  /**
   * The default port to listen on.
   */
  final public static int DEFAULT_PORT = 5555;
  private ChatIF serverUI;
  
  //Constructors ****************************************************
  
  /**
   * Constructs an instance of the echo server.
   *
   * @param port The port number to connect on.
   */
  public EchoServer(int port) 
  {
    this(port, message -> System.out.println(message));
  }

  public EchoServer(int port, ChatIF serverUI)
{
  super(port);
  this.serverUI = serverUI;
}
  
  //Instance methods ************************************************
  
  /**
   * This method handles any messages received from the client.
   *
   * @param msg The message received from the client.
   * @param client The connection from which the message originated.
   */
  public void handleMessageFromClient
    (Object msg, ConnectionToClient client)
  {
    System.out.println("Message received: " + msg + " from " + client);
    this.sendToAllClients(msg);
  }

  /** Displays and broadcasts a message typed in the server console. */
public void handleMessageFromServerUI(String message)
{
  String serverMessage = "SERVER MSG> " + message;

  serverUI.display(serverMessage);
  sendToAllClients(serverMessage);
}



  /**
   * This method overrides the one in the superclass.  Called
   * when the server starts listening for connections.
   */
  protected void serverStarted()
  {
    System.out.println
      ("Server listening for connections on port " + getPort());
  }
  
  @Override
protected void clientConnected(ConnectionToClient client)
{
  client.setInfo("address", client.toString());

  System.out.println(
    "Client conectat: " + client.getInfo("address"));
}

@Override
protected synchronized void clientDisconnected(ConnectionToClient client)
{
  System.out.println(
    "Client deconectat: " + client.getInfo("address"));
}

@Override
protected synchronized void clientException(
    ConnectionToClient client, Throwable exception)
{
  clientDisconnected(client);
}

  /**
   * This method overrides the one in the superclass.  Called
   * when the server stops listening for connections.
   */
  protected void serverStopped()
  {
    System.out.println
      ("Server has stopped listening for connections.");
  }
  
  //Class methods ***************************************************
  
  /**
   * This method is responsible for the creation of 
   * the server console and server instance.
   *
   * @param args[0] The port number to listen on.  Defaults to 5555 
   *          if no argument is entered.
   */
  public static void main(String[] args) 
  {
    ServerConsole.main(args);
  }
}
//End of EchoServer class
