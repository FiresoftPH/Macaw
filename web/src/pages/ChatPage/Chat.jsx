import { useState, useCallback } from "react";
import styles from "./Chat.module.css";
import LongSidebar from "src/components/Sidebar/LongSidebar";
import ShortSideBar from "../../components/Sidebar/ShortSideBar";
import CodeMirror from '@uiw/react-codemirror'

import { EditorView } from "@codemirror/view"
import { javascript } from '@codemirror/lang-javascript'
import { darcula } from '@uiw/codemirror-theme-darcula'

function Chat() {
  const [close, setClose] = useState(false);

  const toggleClose = (val) => {
    setClose((state) => {
      return !state;
    });
  };

  const onChange = useCallback((value,viewUpdate) => {
    console.log('value:', value);
  }, []);
  const fixedHeightEditor = EditorView.theme({
    "&": {height: "40vh"},
    ".cm-content" : { overflow: "auto"},
  })

  return (
    // <div className={`styles.bg_container ` + (close ? "close" : "open")}>
    <div className={`${styles.bg_container} ${close ? styles.close : styles.open}`}>
      {close ? (
        <ShortSideBar open={toggleClose} />
      ) : (
        <LongSidebar close={toggleClose} />
      )}
      <section className={styles.chat}></section>
      <CodeMirror
        className={styles.ide}
        value="console.log('helloworld!')"
        theme={ darcula }
        extensions={[javascript({ jsx:true}), fixedHeightEditor, EditorView.lineWrapping]}
        onChange = { onChange }
      />
      <section className={styles.output}></section>
    </div>
  );
}

export default Chat;
