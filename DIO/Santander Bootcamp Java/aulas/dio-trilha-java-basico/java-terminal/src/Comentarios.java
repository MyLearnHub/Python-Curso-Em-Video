public class Comentarios {
    public static void main(String[] args) {
        // Olá eu sou um comentário em uma única linha

        /* Olá
        * Eu sou um comentário
        * que posso ser mais detalhado
        * quando necessário   
         */
    }

    /**
          * Essas duas estrelinhas acima
          * é para identificar que você pretende elaborar um comentário
          * a nível de documentação
          * Que incrível !!!
          */
          public void metodo(){

          }
          
    public int somaMultiplica(int n, int x, String m){
        int r = 0; // r é igual ao resultado
        if(m == "M"){ // M = multiplicação
            r = n * x;
        } else {
            // Se não soma mesmo
            r = n + x;
        }

        return r;
    }
}
