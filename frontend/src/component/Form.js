import styles from './Form.module.css'

export default function Form (){
    return (
        <form className={styles.form}>
            <label htmFor="input">input text here</label>
            <textarea id="input" rows={5}></textarea>

            <button>Generate video</button>
        </form>
    )
}