package hongsanghee.server.com.example.server.controller;

import hongsanghee.server.com.example.server.dto.Tweet;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
public class SlowServiceController {

    @GetMapping("/api/v1/slow")
    public ResponseEntity<List<Tweet>> slowResponse() {
        List<Tweet> tweets = Arrays.asList(
                new Tweet("1", "Hello World", "Author1"),
                new Tweet("2", "Spring WebFlux", "Author2")
        );

        return ResponseEntity.ok(tweets);
    }
}
