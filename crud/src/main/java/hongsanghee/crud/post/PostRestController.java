package hongsanghee.crud.post;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("post")
public class PostRestController{
    private static final Logger logger= LoggerFactory.getLogger(PostRestController.class);
    private final List<PostDto> postList;
    public PostRestController() {
        this.postList = new ArrayList<>();
    }

    // 1 createPost
    // http://localhost:8080/post
    // POST /post

    @PostMapping()
    public void createPost(@RequestBody PostDto postDto){
        logger.info(postDto.toString());
        this.postList.add(postDto);
    }

    // 2 get
    // http://localhost:8080/post
    // GET /post
    @GetMapping()
    public List<PostDto> readPostAll(){
        logger.info("iin read post all");
        return this.postList;
    }

    // GET /post/0/
    // GET /post?id=0/
    @GetMapping("{id}")
    public PostDto readPost(@PathVariable("id") int id){
        logger.info("in read post");
        return this.postList.get(id);
    }

    //수정하는 RESTFUL API 설계하기
    // PUT /post?id=0처럼 하면 되겠죠..?
    @PutMapping("{id}")
    public void updatePost(@PathVariable("id") int id, @RequestBody PostDto postDto){
        logger.info("in update post");//로그 남기기
        PostDto Post = this.postList.get(id);
        if (Post != null){
            Post.setTitle(postDto.getTitle());
            Post.setContent(postDto.getContent());
            Post.setWriter(postDto.getWriter());
        }

    }
    // Delete하는 RESTFUL API 설계하기
    // DELETE /post?id=0/
    @DeleteMapping("{id}")
    public void deletePost(@PathVariable("id") int id){
        logger.info("in delete post");
        this.postList.remove(id);
    }
}