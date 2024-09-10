package study.querydsl.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import study.querydsl.entity.ProductDetail;

public interface ProductDetailRepository extends JpaRepository<ProductDetail, Long> {
}
