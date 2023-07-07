class CategoryModel:
    def __init__(self, connector):
        self.connector = connector

    def create_category(self, name, status, create_uid, update_uid):
        sql = "INSERT INTO blog_category (name, status, create_uid, update_uid) VALUES (%s, %s, %s, %s)"
        self.connector.execute_update(sql, (name, status, create_uid, update_uid))

    def update_category(self, category_id, name, update_uid):
        sql = "UPDATE blog_category SET name = %s, update_uid = %s WHERE id = %s"
        self.connector.execute_update(sql, (name, update_uid, category_id))

    def delete_category(self, category_id):
        sql = "DELETE FROM blog_category WHERE id = %s"
        self.connector.execute_update(sql, (category_id,))

    def get_category(self, category_id):
        sql = "SELECT * FROM blog_category WHERE id = %s"
        result = self.connector.execute_query(sql, (category_id,))
        return result[0] if result else None
    
    def get_categories_by_conditions(self, conditions):
            sql = "SELECT * FROM blog_category WHERE "
            values = []
            for field, value in conditions.items():
                sql += f"{field} = %s AND "
                values.append(value)
            sql = sql.rstrip("AND ")  # 去除末尾的 "AND"
            result = self.connector.execute_query(sql, tuple(values))
            return result
