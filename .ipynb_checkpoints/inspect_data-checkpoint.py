{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dfb6a8c8-8d3c-4a7e-b8f4-9de41505ea5a",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] Unable to synchronously open file (unable to open file: name = 'your_dataset.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m h5py\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# Open file in read-only mode\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m h5py.File(\u001b[33m\"your_dataset.h5\"\u001b[39m, \u001b[33m\"r\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      5\u001b[39m     \u001b[38;5;66;03m# List all top-level keys\u001b[39;00m\n\u001b[32m      6\u001b[39m     print(\u001b[33m\"Keys in HDF5 file:\"\u001b[39m, list(f.keys()))\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\h5py\\_hl\\files.py:564\u001b[39m, in \u001b[36mFile.__init__\u001b[39m\u001b[34m(self, name, mode, driver, libver, userblock_size, swmr, rdcc_nslots, rdcc_nbytes, rdcc_w0, track_order, fs_strategy, fs_persist, fs_threshold, fs_page_size, page_buf_size, min_meta_keep, min_raw_keep, locking, alignment_threshold, alignment_interval, meta_block_size, **kwds)\u001b[39m\n\u001b[32m    555\u001b[39m     fapl = make_fapl(driver, libver, rdcc_nslots, rdcc_nbytes, rdcc_w0,\n\u001b[32m    556\u001b[39m                      locking, page_buf_size, min_meta_keep, min_raw_keep,\n\u001b[32m    557\u001b[39m                      alignment_threshold=alignment_threshold,\n\u001b[32m    558\u001b[39m                      alignment_interval=alignment_interval,\n\u001b[32m    559\u001b[39m                      meta_block_size=meta_block_size,\n\u001b[32m    560\u001b[39m                      **kwds)\n\u001b[32m    561\u001b[39m     fcpl = make_fcpl(track_order=track_order, fs_strategy=fs_strategy,\n\u001b[32m    562\u001b[39m                      fs_persist=fs_persist, fs_threshold=fs_threshold,\n\u001b[32m    563\u001b[39m                      fs_page_size=fs_page_size)\n\u001b[32m--> \u001b[39m\u001b[32m564\u001b[39m     fid = \u001b[30;43mmake_fid\u001b[39;49m\u001b[30;43m(\u001b[39;49m\u001b[30;43mname\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mmode\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43muserblock_size\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfcpl\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mswmr\u001b[39;49m\u001b[30;43m=\u001b[39;49m\u001b[30;43mswmr\u001b[39;49m\u001b[30;43m)\u001b[39;49m\n\u001b[32m    566\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(libver, \u001b[38;5;28mtuple\u001b[39m):\n\u001b[32m    567\u001b[39m     \u001b[38;5;28mself\u001b[39m._libver = libver\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\h5py\\_hl\\files.py:238\u001b[39m, in \u001b[36mmake_fid\u001b[39m\u001b[34m(name, mode, userblock_size, fapl, fcpl, swmr)\u001b[39m\n\u001b[32m    236\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m swmr \u001b[38;5;129;01mand\u001b[39;00m swmr_support:\n\u001b[32m    237\u001b[39m         flags |= h5f.ACC_SWMR_READ\n\u001b[32m--> \u001b[39m\u001b[32m238\u001b[39m     fid = \u001b[30;43mh5f\u001b[39;49m\u001b[30;43m.\u001b[39;49m\u001b[30;43mopen\u001b[39;49m\u001b[30;43m(\u001b[39;49m\u001b[30;43mname\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mflags\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m=\u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m)\u001b[39;49m\n\u001b[32m    239\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m mode == \u001b[33m'\u001b[39m\u001b[33mr+\u001b[39m\u001b[33m'\u001b[39m:\n\u001b[32m    240\u001b[39m     fid = h5f.open(name, h5f.ACC_RDWR, fapl=fapl)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/_objects.pyx:56\u001b[39m, in \u001b[36mh5py._objects.with_phil.wrapper\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m---> \u001b[39m\u001b[32m56\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/_objects.pyx:57\u001b[39m, in \u001b[36mh5py._objects.with_phil.wrapper\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m---> \u001b[39m\u001b[32m57\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/h5f.pyx:102\u001b[39m, in \u001b[36mh5py.h5f.open\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m--> \u001b[39m\u001b[32m102\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] Unable to synchronously open file (unable to open file: name = 'your_dataset.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)"
     ]
    }
   ],
   "source": [
    "import h5py\n",
    "\n",
    "# Open file in read-only mode\n",
    "with h5py.File(\"your_dataset.h5\", \"r\") as f:\n",
    "    # List all top-level keys\n",
    "    print(\"Keys in HDF5 file:\", list(f.keys()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bef526e7-999a-4cde-887e-7b5ee82a3adf",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] Unable to synchronously open file (unable to open file: name = 'alzheimers_cnn_model.h5.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m h5py\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# Open file in read-only mode\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m h5py.File(\u001b[33m\"alzheimers_cnn_model.h5.h5\"\u001b[39m, \u001b[33m\"r\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      5\u001b[39m     \u001b[38;5;66;03m# List all top-level keys\u001b[39;00m\n\u001b[32m      6\u001b[39m     print(\u001b[33m\"Keys in HDF5 file:\"\u001b[39m, list(f.keys()))\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\h5py\\_hl\\files.py:564\u001b[39m, in \u001b[36mFile.__init__\u001b[39m\u001b[34m(self, name, mode, driver, libver, userblock_size, swmr, rdcc_nslots, rdcc_nbytes, rdcc_w0, track_order, fs_strategy, fs_persist, fs_threshold, fs_page_size, page_buf_size, min_meta_keep, min_raw_keep, locking, alignment_threshold, alignment_interval, meta_block_size, **kwds)\u001b[39m\n\u001b[32m    555\u001b[39m     fapl = make_fapl(driver, libver, rdcc_nslots, rdcc_nbytes, rdcc_w0,\n\u001b[32m    556\u001b[39m                      locking, page_buf_size, min_meta_keep, min_raw_keep,\n\u001b[32m    557\u001b[39m                      alignment_threshold=alignment_threshold,\n\u001b[32m    558\u001b[39m                      alignment_interval=alignment_interval,\n\u001b[32m    559\u001b[39m                      meta_block_size=meta_block_size,\n\u001b[32m    560\u001b[39m                      **kwds)\n\u001b[32m    561\u001b[39m     fcpl = make_fcpl(track_order=track_order, fs_strategy=fs_strategy,\n\u001b[32m    562\u001b[39m                      fs_persist=fs_persist, fs_threshold=fs_threshold,\n\u001b[32m    563\u001b[39m                      fs_page_size=fs_page_size)\n\u001b[32m--> \u001b[39m\u001b[32m564\u001b[39m     fid = \u001b[30;43mmake_fid\u001b[39;49m\u001b[30;43m(\u001b[39;49m\u001b[30;43mname\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mmode\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43muserblock_size\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfcpl\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mswmr\u001b[39;49m\u001b[30;43m=\u001b[39;49m\u001b[30;43mswmr\u001b[39;49m\u001b[30;43m)\u001b[39;49m\n\u001b[32m    566\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(libver, \u001b[38;5;28mtuple\u001b[39m):\n\u001b[32m    567\u001b[39m     \u001b[38;5;28mself\u001b[39m._libver = libver\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\h5py\\_hl\\files.py:238\u001b[39m, in \u001b[36mmake_fid\u001b[39m\u001b[34m(name, mode, userblock_size, fapl, fcpl, swmr)\u001b[39m\n\u001b[32m    236\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m swmr \u001b[38;5;129;01mand\u001b[39;00m swmr_support:\n\u001b[32m    237\u001b[39m         flags |= h5f.ACC_SWMR_READ\n\u001b[32m--> \u001b[39m\u001b[32m238\u001b[39m     fid = \u001b[30;43mh5f\u001b[39;49m\u001b[30;43m.\u001b[39;49m\u001b[30;43mopen\u001b[39;49m\u001b[30;43m(\u001b[39;49m\u001b[30;43mname\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mflags\u001b[39;49m\u001b[30;43m,\u001b[39;49m\u001b[30;43m \u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m=\u001b[39;49m\u001b[30;43mfapl\u001b[39;49m\u001b[30;43m)\u001b[39;49m\n\u001b[32m    239\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m mode == \u001b[33m'\u001b[39m\u001b[33mr+\u001b[39m\u001b[33m'\u001b[39m:\n\u001b[32m    240\u001b[39m     fid = h5f.open(name, h5f.ACC_RDWR, fapl=fapl)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/_objects.pyx:56\u001b[39m, in \u001b[36mh5py._objects.with_phil.wrapper\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m---> \u001b[39m\u001b[32m56\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/_objects.pyx:57\u001b[39m, in \u001b[36mh5py._objects.with_phil.wrapper\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m---> \u001b[39m\u001b[32m57\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mh5py/h5f.pyx:102\u001b[39m, in \u001b[36mh5py.h5f.open\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m--> \u001b[39m\u001b[32m102\u001b[39m \u001b[33m'Could not get source, probably due dynamically evaluated source code.'\u001b[39m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] Unable to synchronously open file (unable to open file: name = 'alzheimers_cnn_model.h5.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)"
     ]
    }
   ],
   "source": [
    "import h5py\n",
    "\n",
    "# Open file in read-only mode\n",
    "with h5py.File(\"alzheimers_cnn_model.h5.h5\", \"r\") as f:\n",
    "    # List all top-level keys\n",
    "    print(\"Keys in HDF5 file:\", list(f.keys()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b535935-eb53-47ff-803e-1ea1e40fa0db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
