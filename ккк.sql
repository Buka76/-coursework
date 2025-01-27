PGDMP      +                |            postgres    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    5    postgres    DATABASE     |   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false            �           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    4825                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            �           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    24599    orderhistory    TABLE     �   CREATE TABLE public.orderhistory (
    id integer NOT NULL,
    "id_заказа" integer,
    "id_робота" integer,
    "Дата" date,
    "Отзыв" text
);
     DROP TABLE public.orderhistory;
       public         heap    postgres    false            �            1259    16417    orders    TABLE     �   CREATE TABLE public.orders (
    id integer NOT NULL,
    "id_отправителя" integer,
    "id_получателя" integer,
    "id_товара" integer,
    "Статус" character(50)
);
    DROP TABLE public.orders;
       public         heap    postgres    false            �            1259    16412    products    TABLE     �   CREATE TABLE public.products (
    id integer NOT NULL,
    "Название" character(50),
    "Описание" character(100),
    "Количество" integer
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16402 	   recipient    TABLE     �   CREATE TABLE public.recipient (
    id integer NOT NULL,
    "ФИО" character(100),
    "Адрес" character(100),
    "Телефон" numeric(11,0)
);
    DROP TABLE public.recipient;
       public         heap    postgres    false            �            1259    16407    robots    TABLE     �   CREATE TABLE public.robots (
    id integer NOT NULL,
    "модель" character(20),
    "местоположение" character(100),
    "id_заказа" integer
);
    DROP TABLE public.robots;
       public         heap    postgres    false            �            1259    16397    sender    TABLE     �   CREATE TABLE public.sender (
    id integer NOT NULL,
    "ФИО" character(100),
    "Телефон" numeric(11,0),
    "Адрес" character(100)
);
    DROP TABLE public.sender;
       public         heap    postgres    false            �          0    24599    orderhistory 
   TABLE DATA           j   COPY public.orderhistory (id, "id_заказа", "id_робота", "Дата", "Отзыв") FROM stdin;
    public          postgres    false    221   �!       �          0    16417    orders 
   TABLE DATA              COPY public.orders (id, "id_отправителя", "id_получателя", "id_товара", "Статус") FROM stdin;
    public          postgres    false    220    "       �          0    16412    products 
   TABLE DATA           f   COPY public.products (id, "Название", "Описание", "Количество") FROM stdin;
    public          postgres    false    219   �"       �          0    16402 	   recipient 
   TABLE DATA           Q   COPY public.recipient (id, "ФИО", "Адрес", "Телефон") FROM stdin;
    public          postgres    false    217   ]#       �          0    16407    robots 
   TABLE DATA           g   COPY public.robots (id, "модель", "местоположение", "id_заказа") FROM stdin;
    public          postgres    false    218   �$       �          0    16397    sender 
   TABLE DATA           N   COPY public.sender (id, "ФИО", "Телефон", "Адрес") FROM stdin;
    public          postgres    false    216   �$       /           2606    16401    sender name_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.sender
    ADD CONSTRAINT name_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.sender DROP CONSTRAINT name_pkey;
       public            postgres    false    216            7           2606    16421    orders orders_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public            postgres    false    220            5           2606    16416    products products_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    219            3           2606    16411    robots robots_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.robots
    ADD CONSTRAINT robots_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.robots DROP CONSTRAINT robots_pkey;
       public            postgres    false    218            9           2606    24609    orderhistory ОrderHistory_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.orderhistory
    ADD CONSTRAINT "ОrderHistory_pkey" PRIMARY KEY (id);
 K   ALTER TABLE ONLY public.orderhistory DROP CONSTRAINT "ОrderHistory_pkey";
       public            postgres    false    221            1           2606    16406    recipient адрес_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.recipient
    ADD CONSTRAINT "адрес_pkey" PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.recipient DROP CONSTRAINT "адрес_pkey";
       public            postgres    false    217            >           2606    32791 "   orderhistory fk_orderhistory_order    FK CONSTRAINT     �   ALTER TABLE ONLY public.orderhistory
    ADD CONSTRAINT fk_orderhistory_order FOREIGN KEY ("id_заказа") REFERENCES public.orders(id);
 L   ALTER TABLE ONLY public.orderhistory DROP CONSTRAINT fk_orderhistory_order;
       public          postgres    false    4663    221    220            ;           2606    32796    orders fk_orders_products    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_orders_products FOREIGN KEY ("id_товара") REFERENCES public.products(id);
 C   ALTER TABLE ONLY public.orders DROP CONSTRAINT fk_orders_products;
       public          postgres    false    220    219    4661            <           2606    32801    orders fk_orders_recipient    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_orders_recipient FOREIGN KEY ("id_получателя") REFERENCES public.recipient(id);
 D   ALTER TABLE ONLY public.orders DROP CONSTRAINT fk_orders_recipient;
       public          postgres    false    4657    217    220            =           2606    32806    orders fk_orders_sender    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_orders_sender FOREIGN KEY ("id_отправителя") REFERENCES public.sender(id);
 A   ALTER TABLE ONLY public.orders DROP CONSTRAINT fk_orders_sender;
       public          postgres    false    216    220    4655            :           2606    32811    robots fk_robots_orders    FK CONSTRAINT     �   ALTER TABLE ONLY public.robots
    ADD CONSTRAINT fk_robots_orders FOREIGN KEY ("id_заказа") REFERENCES public.orders(id);
 A   ALTER TABLE ONLY public.robots DROP CONSTRAINT fk_robots_orders;
       public          postgres    false    218    220    4663            �   H   x�3�4�4�4202�50�54漰�bÅ��}6]� ��$��	�)Tr�D�*�����n�=... �!�      �   a   x�3�4�4�4�0�b˅}.칰���{�\F�F@�8/L�x���H4�˘/LR���b3АĻ ���S��`

2����� �ET�      �   �   x���M
�0�יSx��?�iz�RzA�^�͍��.fx�73���%V�p�'�$�,��Ƌ�:&����yP��i�o���yĬ�$���P��7�����Rd�|���V`�.ъ�3C�g�z�L
C��V}4aІ��i�0����-����<�Y�9��6ԝ��&��~��!�      �     x�œ[N�0���*� cz���bM��D��utUg"���yZ!�̃/5��p(�w��]��.��1�Ub������ �L������2�U���I���-�_"�Ɉ��u�JW��8+L����>s�W=>$n���c��+I^����G�VeCMĺq:�[W	���Zsl9�.y���)��-�>O#_/3{sd���~�W�3�RN�V�ڲ��%]ӂ�-�)k^��O���:k$��W���7����5>Ƒ�?�����)�|�g�B�/����      �   g   x�3�2R� �f]�w������u.캰���;.콰�b����
�)�1g���)^���)F\&�A�X$�
����)�\��P!����	W� c��]      �     x�œKN�0D��)r ����8w�0�a���`�g�,X�a"F��P}#�M�8�Qz�mKU�]���a��\����C_➿�l���Q[��;r�O����Ll��5�o�5x�D�/9�uuR��%�XV6���*V/Is�،�U�t!�J����m�*ڰ �3�!ݧr����@��4�w~r�[��ֻCp~lj�*!#�[p�5�G�i��g�`,x.��g��B_����ܥ�.-�p��J�F���d�yۆ&. vZ�7[?�S     