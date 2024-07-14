import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import javax.crypto.Cipher;

public class AdvancedCryptography {
  public static void main(String[] args) throws Exception {
    KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
    kpg.initialize(2048);
    KeyPair kp = kpg.generateKeyPair();
    PrivateKey privateKey = kp.getPrivate();
    PublicKey publicKey = kp.getPublic();

    String message = "This is a secret message";
    byte[] encryptedMessage = encrypt(message, publicKey);
    System.out.println("Encrypted message: " + encryptedMessage);

    byte[] decryptedMessage = decrypt(encryptedMessage, privateKey);
    System.out.println("Decrypted message: " + new String(decryptedMessage));
  }

  public static byte[] encrypt(String message, PublicKey publicKey) throws Exception {
    Cipher cipher = Cipher.getInstance("RSA");
    cipher.init(Cipher.ENCRYPT_MODE, publicKey);
    return cipher.doFinal(message.getBytes());
  }

  public static byte[] decrypt(byte[] encryptedMessage, PrivateKey privateKey) throws Exception {
    Cipher cipher = Cipher.getInstance("RSA");
    cipher.init(Cipher.DECRYPT_MODE, privateKey);
    return cipher.doFinal(encryptedMessage);
  }
}
