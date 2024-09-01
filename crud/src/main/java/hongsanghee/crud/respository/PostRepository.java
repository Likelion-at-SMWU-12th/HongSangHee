package hongsanghee.crud.respository;

import hongsanghee.crud.entity.PostEntity;
import org.springframework.data.repository.CrudRepository;

public interface PostRepository extends CrudRepository<PostEntity, Long> {
}