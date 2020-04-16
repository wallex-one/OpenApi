import com.google.common.base.Joiner;
import lombok.extern.slf4j.Slf4j;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.apache.commons.codec.binary.Hex;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;
import java.util.TreeMap;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;

@Slf4j
public class OrgApiTest {

	// FIXME: change these for your need
	private static final String domain = "https://api.tsc100.vip";

	private static final String apiKey = "xxxxxxxxxxxx";
	private static final String apiSecret = "xxxxxxxxxxx";

	private static OkHttpClient okHttpClient
			= new OkHttpClient.Builder()
			.connectTimeout(2, TimeUnit.SECONDS)
			.writeTimeout(5, TimeUnit.SECONDS)
			.readTimeout(5, TimeUnit.SECONDS)
			.build();
	private static AtomicLong idGen = new AtomicLong(System.currentTimeMillis());

	// DO NOT change these
	private static final String API_KEY_HEADER = "X-ACCESS-KEY";
	String apiUrlPrefix = domain + "/api/v2/org";

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testTransferAPI() {
		Request.Builder requestBuilder = new Request.Builder();

		TreeMap<String, String> paramsMap = new TreeMap<>();
		paramsMap.put("client_order_id", String.valueOf(System.currentTimeMillis()));
		paramsMap.put("source_user_id", "376025805823958016");
		paramsMap.put("target_user_id", "376025805823958016");
		paramsMap.put("token_id", "ALGO");
		paramsMap.put("amount", "1.23");
		paramsMap.put("from_source_lock", "false");
		paramsMap.put("to_target_lock", "true");
		paramsMap.put("business_subject", "70"); // 3: transfer; 70: airdrop
		paramsMap.put("sub_business_subject", "0"); // set if necessary
		paramsMap.put("signature", sign(paramsMap, apiSecret));

		FormBody.Builder paramBuilder = new FormBody.Builder();
		for (String s : paramsMap.keySet()) {
			paramBuilder.add(s, paramsMap.get(s));
		}


		requestBuilder.url(apiUrlPrefix + "/finance/transfer").post(paramBuilder.build());

		// add apiKey header
		requestBuilder.addHeader(API_KEY_HEADER, apiKey);

		// sign the request
		Request finalRequest = requestBuilder.build();

		try (Response response = okHttpClient.newCall(finalRequest).execute()) {
			if (response.isSuccessful()) {
				String responseData = response.body().string();
				// todo parse the response body data
				log.info("call url {} \n param {} \n return {}", finalRequest.url(), paramsMap, responseData);
			} else {
				// todo log the error response
				log.warn("call url {} \n param {} \n return {}", finalRequest.url(), paramsMap, response.toString());
				Assert.fail();
			}
		} catch (IOException e) {
			// todo deal with the network error
			log.error("call url {} \n param {} \n return exception {}", finalRequest.url(), paramsMap, e.toString());
			Assert.fail();
		}

	}

	private static String sign(TreeMap<String, String> requestParamMap, String secret) {
		try {
			String originalStr = Joiner.on("&").withKeyValueSeparator("=").join(requestParamMap);
			log.info(originalStr);
			Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
			SecretKeySpec secretKeySpec = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
			sha256_HMAC.init(secretKeySpec);
			return new String(Hex.encodeHex(sha256_HMAC.doFinal(originalStr.getBytes())));
		} catch (Exception e) {
			throw new RuntimeException("Unable to sign message.", e);
		}
	}

}