package hongsanghee.client.controller;

import hongsanghee.client.dto.MemberDto;
import hongsanghee.client.service.WebClientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/web-controller")
public class WebClientController {

    @Autowired
    private WebClientService webClientService;

    @GetMapping("/path-variable")
    public Mono<String> getPathVariable(){
        return webClientService.getNameWithPathVariable();
    }

    @GetMapping("/parameter")
    public Mono<MemberDto> getParameter(){
        return webClientService.postWithParamAndBody();
    }

    @GetMapping("/header")
    public Mono<MemberDto> getHeader(){
        return webClientService.postWithHeader();
    }
}
