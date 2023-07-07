from database.mysql_connector import connector

def main():
    sql = """
    CREATE TABLE IF NOT EXISTS `blog_category` (
        `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增ID',
        `name`          VARCHAR(255) NOT NULL DEFAULT '' COMMENT   '分类名称',
        `status`        TINYINT(1)   NOT NULL DEFAULT 1  COMMENT   '是否启用，0弃用，1启用',
        `create_uid`    INT(11) NOT NULL DEFAULT 0 COMMENT '创建者',
        `update_uid`    INT(11) NOT NULL DEFAULT 0 COMMENT '编辑者',
        `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
        `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
        PRIMARY KEY (`id`) USING BTREE
    )
    ENGINE=InnoDB
    CHARSET='utf8mb4'
    COLLATE='utf8mb4_unicode_ci'
    COMMENT='博客模块-分类表'
    ;
    """
    try:
        connector.create_database_if_not_exists(sql)
        print("Table created successfully!")
    except Exception as e:
        print(f"Error creating table: {str(e)}")


if __name__ == '__main__':
    main()