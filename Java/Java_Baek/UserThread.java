public class UserThread extends Thread {
    public UserThread(String name){
        super(name);
    }

    public void run(){
        Printer printer = Printer.getPrinter();
        printer.print(Thread.currentThread().getName() + " print using " + printer.toString() + ".");
    }
}

public class Printer{
    private static Printer printer = null;
    private Printer(){}
    
    public static Printer getPrinter(){
        if(printer == null){
            try{ Thread.sleep(1);
            }

            catch(InterruptedException e){}
            printer = new Printer();
        }
        return printer;
    }
    
    public void print(String str){
        System.out.println(str);
    }
}