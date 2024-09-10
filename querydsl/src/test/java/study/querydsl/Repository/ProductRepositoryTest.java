package study.querydsl.Repository;

import com.querydsl.jpa.impl.JPAQueryFactory;
import jakarta.persistence.EntityManager;
import jakarta.transaction.Transactional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.data.domain.PageRequest;
import study.querydsl.entity.Product;
import study.querydsl.entity.QProduct;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@DataJpaTest
@Transactional
class ProductRepositoryTest {

    @Autowired
    private ProductRepository productRepository;

    @Autowired
    EntityManager entityManager;

    //@BeforeEach를 사용하여 각 테스트 전에 더미 데이터 삽입
    @BeforeEach
    void setUp(){
        productRepository.save(new Product("펜", 1000, 100,1));
        productRepository.save(new Product("연필", 500, 200,2));
        productRepository.save(new Product("노트", 2000, 150,3));
        productRepository.save(new Product("지우개", 300, 300,4));
        productRepository.save(new Product("자", 750, 250,5));
        productRepository.save(new Product("기아", 12000, 10,100));
        productRepository.save(new Product("다크 초콜릿", 5000, 50, 11));
        productRepository.save(new Product("화이트 초콜릿", 5500, 40, 14));
        productRepository.save(new Product("아몬드 초콜릿", 7000, 30, 13));
        productRepository.save(new Product("카라멜 초콜릿", 6500, 45, 12));
        productRepository.save(new Product("모카 초콜릿", 7500, 35, 65));
        productRepository.save(new Product("민트 초콜릿", 5000, 55, 6));
        productRepository.save(new Product("피넛버터 초콜릿", 5000, 50, 10));
        productRepository.save(new Product("코코넛 초콜릿", 5000, 50, 8));
        productRepository.save(new Product("트러플 초콜릿", 5000, 50, 15));
        productRepository.save(new Product("헤이즐넛 초콜릿", 5000, 50, 9));
        productRepository.save(new Product("라즈베리 초콜릿", 5000, 50, 7));
        productRepository.save(new Product("위스키 봉봉", 15000, 50, 77));



    }

    @Test
    void queryDslTest(){
        JPAQueryFactory jpaQuery = new JPAQueryFactory(entityManager);
        QProduct qProduct = QProduct.product;

        List<Product> productList =
                jpaQuery.selectFrom(qProduct)
                        .where(qProduct.name.eq("펜"))
                        .orderBy(qProduct.price.asc())
                        .fetch();

        for(Product product : productList){
            System.out.println("--------------------");
            System.out.println("Product Number : " + product.getId());
            System.out.println("Product Name : " + product.getName());
            System.out.println("Product Price : " + product.getPrice());
            System.out.println("Product Stock : " + product.getStock());
            System.out.println("--------------------");
        }
    }

    @Test
    void popularityTest(){
        List<Product> populariList = productRepository.findTop10ByOrderByPopularityDesc();
        for(Product product : populariList){
            System.out.println("--------------------");
            System.out.println("Product Popularity : " + product.getPopularity());
            System.out.println("Product Name : " + product.getName());
            System.out.println("--------------------");

        }
    }

    @Test
    void productLatestTest(){
        PageRequest pageRequest = PageRequest.of(0, 10);
        List<Product> latesttList = productRepository.findTop10LatestProducts(pageRequest);
        for(Product product : latesttList){
            System.out.println("--------------------");
            System.out.println("Product Name : " + product.getName());
            System.out.println("Product Id : " + product.getId());
            System.out.println("--------------------");
        }
    }
}