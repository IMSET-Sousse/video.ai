import styles from "./Video.module.css"


export default function Video(){

    return(
        <video className={styles.videoPlayer} width="400" controls>
            <source src="mov_bbb.mp4" type="video/mp4" />
        </video>
    )
}