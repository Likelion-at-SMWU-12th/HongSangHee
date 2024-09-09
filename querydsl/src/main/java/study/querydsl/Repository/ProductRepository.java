package study.querydsl.Repository;

import jakarta.persistence.EntityManager;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import study.querydsl.entity.Product;

import java.util.List;

public interface ProductRepository extends JpaRepository<Product, Long> {
    // JPA를 활용하여 쿼리 메소드를 통해 인기도 TOP 10 반환하기
}
