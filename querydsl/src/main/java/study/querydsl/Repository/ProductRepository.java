package study.querydsl.Repository;

import jakarta.persistence.EntityManager;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import study.querydsl.entity.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {

}
