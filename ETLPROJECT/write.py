def to_files(df, tgt_dir, file_format):
    df.coalesce(16). \
        write. \
        partitionBy('product_id'). \
        mode('append'). \
        format(file_format). \
        save(tgt_dir)

