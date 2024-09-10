package study.querydsl.Repository;

import jakarta.persistence.EntityManager;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import study.querydsl.entity.Product;

import java.util.List;

public interface ProductRepository extends JpaRepository<Product, Long> {
    //인기순 top 10
    List<Product> findTop10ByOrderByPopularityDesc();

    //등록순 top 10
    @Query("SELECT p FROM Product p ORDER BY p.id DESC")
    List<Product> findTop10LatestProducts(PageRequest pageRequest);

}
