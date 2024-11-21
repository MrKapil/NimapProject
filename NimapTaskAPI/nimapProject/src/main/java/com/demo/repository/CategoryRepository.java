package com.demo.repository;


import org.springframework.data.jpa.repository.JpaRepository;

import com.demo.model.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {  
}

//used for inherits CRUD methods from JpaRepository // 
